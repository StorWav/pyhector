/*
 * Copyright (c) 2017 - 2024 Sven Willner <sven.willner@gmail.com>
 * Free software under GNU Affero General Public License v3, see LICENSE
 */

#include "Hector.h"

#include <pybind11/numpy.h>

#include <stdexcept>
#include <sstream>
#include <iostream>

#include "component_data.hpp"
#include "h_exception.hpp"
#include "message_data.hpp"
#include "unitval.hpp"
#include "logger.hpp"

namespace hector = Hector;
namespace py = pybind11;

namespace pyhector {

Hector::Visitor::~Visitor() = default;

void Hector::Visitor::reset(const double reset_date) {
    // std::cout << "Hector::reset()" << " " << __FILE__ << ":" << __LINE__ << " " << reset_date << "\n";
    current_date = reset_date;
}

bool Hector::Visitor::shouldVisit(bool in_spinup, double date) {
    // std::cout << "Hector::shouldVisit()" << " " << __FILE__ << ":" << __LINE__ << " " << in_spinup << " " << date << "\n";
    // if in_spinup is true, date starts from 1, but last value is the start date (then hcore->inSpinup() is false already)
    // if in_spinup is false, date starts from start date + 1
    current_date = date;
    return true;
}

void Hector::Visitor::visit(hector::Core* hcore) {
    if (std::isnan(current_date)) {
        return;  // unfortunately, Hector calls visit with date 0 before shouldVisit
    }
    // unfortunately hcore->getCurrentDate() does not work (it always yields the start date)
    std::size_t index;
    if (hcore->inSpinup()) {
        index = static_cast<std::size_t>(current_date - 1);
        if (index != spinup_size) {
            throw std::runtime_error("Spinup size mismatch");
        }
    } else {
        const auto start_date = hcore->getStartDate();
        if (start_date > current_date) {
            throw std::runtime_error("Start date is after current date");
        }
        index = static_cast<std::size_t>(current_date - start_date);
        // std::cout << "Hector::visit()" << " " << __FILE__ << ":" << __LINE__ << " " << start_date << " " << current_date << " " << index << "\n";
    }
    for (auto& observable : observables) {
        observable.read_data(hcore, current_date, index);
    }
    if (hcore->inSpinup()) {
        ++spinup_size;
    }
}

hector::Core* Hector::core() {
    if (!core_) {
        // reset();
        mkcore(py::none(), py::none(), py::none());
    }
    return core_.get();
}

void Hector::add_observable(std::string component, std::string name, bool needs_date, bool in_spinup) {
    visitor.observables.emplace_back(Observable{core(), std::move(component), std::move(name), needs_date, in_spinup, run_size()});
}

py::array_t<double> Hector::get_observable(const std::string& component, const std::string& name, const bool in_spinup) const {
    for (const auto& observable : visitor.observables) {
        if (observable.matches(component, name, in_spinup)) {
            return observable.get_array();
        }
    }
    throw std::runtime_error("Observable not found");
}

double Hector::current_value(const std::string& component, const std::string& name, bool in_spinup) {
    for (const auto& observable : visitor.observables) {
        if (observable.matches(component, name, in_spinup)) {
            if (start_date() > current_date()) {
                throw std::runtime_error("Start date is after current date");
            }
            std::size_t index = static_cast<std::size_t>(current_date() - start_date());
            return observable.value_at(index);
        }
    }
    throw std::runtime_error("Observable not found");
}

void Hector::clear_observables() { visitor.observables.clear(); }

std::size_t Hector::run_size() { return static_cast<std::size_t>(std::max(0.0, core()->getEndDate() - core()->getStartDate())); }

std::size_t Hector::spinup_size() const { return visitor.spinup_size; }

double Hector::end_date() { return core()->getEndDate(); }

double Hector::start_date() { return core()->getStartDate(); }

double Hector::current_date() { return visitor.current_date; }

void Hector::prepareToRun() {
    visitor.spinup_size = 0;
    core()->prepareToRun();
}

void Hector::reset(const py::object& until) {
    core()->reset(until.is_none() ? -1 : until.cast<double>());
}

void Hector::run(const py::object& until) {
    core()->run(until.is_none() ? -1 : until.cast<double>());
}

void Hector::shutdown() {
    core()->shutDown();
    core_.reset();
}

void Hector::mkcore(const py::object& loglvl, const py::object& logtofile, const py::object& logtoscrn) {
    // core_.reset(new hector::Core(hector::Logger::WARNING, false, false));
    hector::Logger::LogLevel loglevel = hector::Logger::WARNING;
    if (!loglvl.is_none()) 
        loglevel = static_cast<hector::Logger::LogLevel>(loglvl.cast<int>());
    core_.reset(new hector::Core(loglevel, logtoscrn.is_none() ? false : logtoscrn.cast<bool>(), logtofile.is_none() ? false : logtofile.cast<bool>()));
    core_->init();
    core_->addVisitor(&visitor);
    for (auto& observable : visitor.observables) {
        observable.reset(core_.get());
    }
}

void Hector::set(const std::string& section, const std::string& variable, const std::string& value) {
    hector::message_data data(value);
    auto bracket_open = std::find(variable.begin(), variable.end(), '[');
    if (bracket_open != variable.end()) {
        data.date = std::stod(std::string(bracket_open + 1, std::find(bracket_open, variable.end(), ']')));
        core()->setData(section, std::string(variable.begin(), bracket_open), data);
    } else {
        hector::message_data data(value);
        core()->setData(section, variable, data);
    }
}

void Hector::set(const std::string& section, const std::string& variable, double value) {
    hector::message_data data(hector::unitval(value, hector::U_UNDEFINED));
    core()->setData(section, variable, data);
}

void Hector::set(const std::string& section, const std::string& variable, std::size_t year, double value) {
    hector::message_data data(hector::unitval(value, hector::U_UNDEFINED));
    data.date = year;
    core()->setData(section, variable, data);
}

void Hector::set(const std::string& section, const std::string& variable, const std::size_t* years, const double* values, size_t size) {
    for (std::size_t i = 0; i < size; ++i) {
        hector::message_data data(hector::unitval(values[i], hector::U_UNDEFINED));
        data.date = years[i];
        core()->setData(section, variable, data);
    }
}

void Hector::set(const std::string& section, const std::string& variable, const std::vector<std::size_t>& years, const std::vector<double>& values) {
    if (years.size() != values.size()) {
        throw std::runtime_error("years and values should be of equal size");
    }
    set(section, variable, &years[0], &values[0], years.size());
}

void Hector::set(const std::string& section, const std::string& variable, double value, const std::string& unit) {
    hector::message_data data(hector::unitval(value, hector::unitval::parseUnitsName(unit)));
    core()->setData(section, variable, data);
}

void Hector::set(const std::string& section, const std::string& variable, std::size_t year, double value, const std::string& unit) {
    hector::message_data data(hector::unitval(value, hector::unitval::parseUnitsName(unit)));
    data.date = year;
    core()->setData(section, variable, data);
}

void Hector::set(
    const std::string& section, const std::string& variable, const std::size_t* years, const double* values, size_t size, const std::string& unit) {
    for (std::size_t i = 0; i < size; ++i) {
        hector::message_data data(hector::unitval(values[i], hector::unitval::parseUnitsName(unit)));
        data.date = years[i];
        core()->setData(section, variable, data);
    }
}

void Hector::set(const std::string& section,
                 const std::string& variable,
                 const std::vector<std::size_t>& years,
                 const std::vector<double>& values,
                 const std::string& unit) {
    if (years.size() != values.size()) {
        throw std::runtime_error("years and values should be of equal size");
    }
    set(section, variable, &years[0], &values[0], years.size(), unit);
}

}  // namespace pyhector
