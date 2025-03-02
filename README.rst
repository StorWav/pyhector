pyhector
========

+----------------+------------------------+
| |PyPI Version| | |PyPI Python Versions| |
+----------------+------------------------+
| |Docs|         | |Launch Binder|        |
+----------------+------------------------+
| |JOSS|         | |Zenodo|               |
+----------------+------------------------+

.. sec-begin-index

**pyhector** is a Python interface for the simple global climate
carbon-cycle model `Hector <https://github.com/JGCRI/hector>`_.

**pyhector** makes the simple climate model Hector easily installable
and usable from Python and can for example be used in the analysis of
mitigation scenarios, in integrated assessment models, complex climate
model emulation, and uncertainty analyses.

`Hector <https://github.com/JGCRI/hector>`_ is written in C++ and
developed at the `Pacific Northwest National Laboratory
<https://www.pnnl.gov/>`_.

See the Hector `repository <https://github.com/JGCRI/hector>`_ and
`documentation website <https://jgcri.github.io/hector/>`_ for further
information.

The Python interface **pyhector** is developed by `Sven Willner
<http://svenwillner.com>`_ and `Robert Gieseke
<https://github.com/rgieseke>`_.

Pyhector uses `pybind11 <https://github.com/pybind/pybind11>`_ to wrap
Hector's API. The version of Hector used can be read using Pyhector's
``__hector_version__`` field.

.. sec-end-index
.. sec-begin-installation

Installation
------------

Prerequisites
~~~~~~~~~~~~~

`Hector <https://github.com/JGCRI/hector>`_ requires `Boost
<http://www.boost.org/>`_, so to install and use **pyhector** you need
to have the filesystem and system modules of *Boost* installed (see also the `Hector build
instructions <https://jgcri.github.io/hector/articles/BuildHector.html#standalone-executable>`_).

On Ubuntu/Debian these can be installed by invoking

.. code:: bash

    sudo apt-get install libboost-filesystem-dev libboost-system-dev

On macOS *Boost* is available through the Homebrew package manager, it
might be advisable to use a Homebrew installed Python for installing
**pyhector**:

.. code:: bash

    brew install boost

Windows is (as Hector) in principle supported but not yet tested for
**pyhector**. Pull request with installation notes for Windows are
welcome.

Install using pip
~~~~~~~~~~~~~~~~~

You can install **pyhector** from
`PyPI <https://pypi.python.org/pypi/pyhector>`_ by invoking

.. code:: bash

    pip install pyhector

.. sec-end-installation
.. sec-begin-usage

Usage
-----

This repository also contains a `Jupyter Notebook
<https://jupyter.readthedocs.io/en/latest/index.html>`_ you can `run
live <http://mybinder.org/repo/openclimatedata/pyhector>`_ and
experiment with, courtesy of the `Binder <http://mybinder.org/>`_
project. The notebook can be viewed as a `static version
<http://nbviewer.jupyter.org/github/openclimatedata/pyhector/blob/main/index.ipynb>`_
using nbviewer.

Basic example
~~~~~~~~~~~~~

.. code:: python

    import pyhector

    output = pyhector.run(pyhector.ssp126)

Advanced example
~~~~~~~~~~~~~~~~

.. code:: python

    import pyhector
    import matplotlib.pyplot as plt
    from pyhector import ssp119, ssp126, ssp245, ssp370, ssp434, ssp460, ssp534_over, ssp585

    for ssp in [ssp119, ssp126, ssp245, ssp370, ssp434, ssp460, ssp534_over, ssp585]:
        output = pyhector.run(ssp, {"core": {"endDate": 2100}})
        temp = output["temperature.global_tas"]
        temp = temp.loc[1850:] - temp.loc[1850:1900].mean()
        temp.plot(label=ssp.name)
    plt.title("Global mean temperature")
    plt.ylabel("°C over pre-industrial (1850-1900 mean)")
    plt.legend(loc="best")
    plt.show()

.. image-start

.. image:: ./docs/example-plot.png
    :alt: Temperature Plot of RCP scenarios

.. image-end
.. sec-end-usage
.. sec-begin-development

Development
-----------

For local development you can clone the repository, update the
dependencies and install in a virtual environment with ``pip``.

.. code:: bash

    git clone https://github.com/openclimatedata/pyhector.git --recursive
    cd pyhector
    python3 -m venv venv
    ./venv/bin/pip install --editable --verbose .


To update **pyhector** and all submodules you can run

.. code:: bash

    git pull --recurse-submodules
    git submodule update --init --recursive
    ./venv/bin/pip install --editable .

Tests can be run locally with

::

    python setup.py test

.. sec-end-development

.. |PyPI Python Versions| image:: https://img.shields.io/pypi/pyversions/pyhector.svg
   :target: https://pypi.org/project/pyhector/
.. |PyPI Version| image:: https://img.shields.io/pypi/v/pyhector.svg
   :target: https://pypi.org/project/pyhector/
.. |Docs| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat
   :target: https://pyhector.readthedocs.io/en/latest/
.. |Launch Binder| image:: https://img.shields.io/badge/launch-binder-e66581.svg
   :target: https://mybinder.org/v2/gh/openclimatedata/pyhector/main?filepath=notebooks/index.ipynb
.. |JOSS| image:: https://img.shields.io/badge/JOSS-10.21105%2Fjoss.00248-brightgreen.svg
   :target: https://doi.org/10.21105/joss.00248
.. |Zenodo| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1194599.svg
   :target: https://zenodo.org/record/1194599
