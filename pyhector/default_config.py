"""Dictionary with default config."""

_default_config = {
    "C2F6_halocarbon": {
        "delta_C2F6": 0.0,
        "molarMass": 138.01,
        "rho_C2F6": 0.000261,
        "tau": 10000.0,
    },
    "CCl4_halocarbon": {
        "delta_CCl4": 0.0,
        "molarMass": 153.8,
        "rho_CCl4": 0.000166,
        "tau": 32.0,
    },
    "CF4_halocarbon": {
        "H0": 35.0,
        "delta_CF4": 0.0,
        "molarMass": 88.0043,
        "rho_CF4": 9.9e-05,
        "tau": 50000.0,
    },
    "CFC113_halocarbon": {
        "delta_CFC113": 0.0,
        "molarMass": 187.35,
        "rho_CFC113": 0.000301,
        "tau": 93.0,
    },
    "CFC114_halocarbon": {
        "delta_CFC114": 0.0,
        "molarMass": 170.9,
        "rho_CFC114": 0.000314,
        "tau": 189,
    },
    "CFC115_halocarbon": {
        "delta_CFC115": 0.0,
        "molarMass": 154.45,
        "rho_CFC115": 0.000246,
        "tau": 540,
    },
    "CFC11_halocarbon": {
        "delta_CFC11": 0.13,
        "molarMass": 137.35,
        "rho_CFC11": 0.000259,
        "tau": 52.0,
    },
    "CFC12_halocarbon": {
        "delta_CFC12": 0.13,
        "molarMass": 120.9,
        "rho_CFC12": 0.00032,
        "tau": 102.0,
    },
    "CH3Br_halocarbon": {
        "H0": 5.8,
        "delta_CH3Br": 0.0,
        "molarMass": 50.45,
        "rho_CH3Br": 4e-06,
        "tau": 0.8,
    },
    "CH3CCl3_halocarbon": {
        "delta_CH3CCl3": 0.0,
        "molarMass": 133.35,
        "rho_CH3CCl3": 6.5e-05,
        "tau": 5.0,
    },
    "CH3Cl_halocarbon": {
        "H0": 504.0,
        "delta_CH3Cl": 0.0,
        "molarMass": 50.45,
        "rho_CH3Cl": 5e-06,
        "tau": 0.9,
    },
    "CH4": {"CH4N": 335, "M0": 731.41, "Tsoil": 160, "Tstrat": 120, "UC_CH4": 2.78},
    "HCFC141b_halocarbon": {
        "delta_HCFC141b": 0.0,
        "molarMass": 116.9,
        "rho_HCFC141b": 0.000161,
        "tau": 9.4,
    },
    "HCFC142b_halocarbon": {
        "delta_HCFC142b": 0.0,
        "molarMass": 100.45,
        "rho_HCFC142b": 0.000193,
        "tau": 18.0,
    },
    "HCFC22_halocarbon": {
        "delta_HCFC22": 0.0,
        "molarMass": 86.45,
        "rho_HCFC22": 0.000214,
        "tau": 11.9,
    },
    "HFC125_halocarbon": {
        "delta_HFC125": 0.0,
        "molarMass": 120.02,
        "rho_HFC125": 0.000234,
        "tau": 30.0,
    },
    "HFC134a_halocarbon": {
        "delta_HFC134a": 0.0,
        "molarMass": 102.02,
        "rho_HFC134a": 0.000167,
        "tau": 14.0,
    },
    "HFC143a_halocarbon": {
        "delta_HFC143a": 0.0,
        "molarMass": 84.04,
        "rho_HFC143a": 0.000168,
        "tau": 51.0,
    },
    "HFC227ea_halocarbon": {
        "delta_HFC227ea": 0.0,
        "molarMass": 170.03,
        "rho_HFC227ea": 0.000273,
        "tau": 36.0,
    },
    "HFC23_halocarbon": {
        "delta_HFC23": 0.0,
        "molarMass": 70.0,
        "rho_HFC23": 0.000191,
        "tau": 228.0,
    },
    "HFC245fa_halocarbon": {
        "delta_HFC245fa": 0.0,
        "molarMass": 134.0,
        "rho_HFC245fa": 0.000245,
        "tau": 7.9,
    },
    "HFC32_halocarbon": {
        "delta_HFC32": 0.0,
        "molarMass": 52.0,
        "rho_HFC32": 0.000111,
        "tau": 5.4,
    },
    "HFC4310_halocarbon": {
        "delta_HFC4310": 0.0,
        "molarMass": 252.0,
        "rho_HFC4310": 0.000357,
        "tau": 17.0,
    },
    "N2O": {
        "N0": 273.87,
        "N2O_natural_emissions": [(1750, 9.72)],
        "TN2O0": 132,
        "UC_N2O": 4.8,
    },
    "OH": {
        "CCH4": -0.32,
        "CCO": -0.000105,
        "CNMVOC": -0.000315,
        "CNOX": 0.0042,
        "TOH0": 6.6,
    },
    "SF6_halocarbon": {
        "delta_SF6": 0.0,
        "molarMass": 146.06,
        "rho_SF6": 0.000567,
        "tau": 3200.0,
    },
    "carbon-cycle-solver": {
        "dt": 0.25,
        "eps_abs": 1e-06,
        "eps_rel": 1e-06,
        "eps_spinup": 0.001,
    },
    "core": {
        "do_spinup": True,
        "endDate": 2300,
        "max_spinup": 2000,
        "run_name": "pyhector-run",
        "startDate": 1745,
        "trackingDate": 9999,
    },
    "forcing": {
        "RF_misc": [(1750, 0)],
        "baseyear": 1750,
        "delta_ch4": -0.14,
        "delta_co2": 0.05,
        "delta_n2o": 0.07,
        "rho_bc": 0.06386286,
        "rho_nh3": -0.002146032,
        "rho_oc": -0.006407143,
        "rho_so2": -7.469841e-06,
    },
    "halon1211_halocarbon": {
        "delta_halon1211": 0.0,
        "molarMass": 165.35,
        "rho_halon1211": 3e-05,
        "tau": 16.0,
    },
    "halon1301_halocarbon": {
        "delta_halon1301": 0.0,
        "molarMass": 148.9,
        "rho_halon1301": 0.000299,
        "tau": 72.0,
    },
    "halon2402_halocarbon": {
        "delta_halon2402": 0.0,
        "molarMass": 259.8,
        "rho_halon2402": 0.000312,
        "tau": 28.0,
    },
    "ocean": {
        "enabled": True,
        "preind_interdeep_c": 37100,
        "preind_surface_c": 900,
        "spinup_chem": 0,
        "tid": 200000000,
        "tt": 72000000,
        "tu": 49000000,
        "twi": 12500000,
    },
    "ozone": {"PO3": 30.0},
    "simpleNbox": {
        "C0": 277.15,
        "atmos_co2": 590.33,
        "beta": 0.53,
        "detritus_c": 55,
        "f_litterd": 0.98,
        "f_nppd": 0.6,
        "f_nppv": 0.35,
        "npp_flux0": 56.2,
        "permafrost_c": 865,
        "q10_rh": 1.76,
        "soil_c": 917,
        "veg_c": 550,
    },
    "so2": {
        "SV": [
            (1745, 0.1857456741581203),
            (1746, 0.1857456741581203),
            (1747, 0.1857456741581203),
            (1748, 0.1857456741581203),
            (1749, 0.1857456741581203),
            (1750, 0.1857456741581203),
            (1751, 0.1857567460517512),
            (1752, 0.1857604715824308),
            (1753, 0.1857617169069504),
            (1754, 0.1857621356409382),
            (1755, 0.1614905100426892),
            (1756, -0.0641399037555059),
            (1757, 0.0654814896339625),
            (1758, 0.143706674085902),
            (1759, 0.1715602637374792),
            (1760, 0.180988300871404),
            (1761, 0.1841585443588585),
            (1762, -0.7198788864817063),
            (1763, -0.4399601212913509),
            (1764, -0.0390473245778303),
            (1765, 0.1095816660972169),
            (1766, -0.1784875267041926),
            (1767, -0.230039677074036),
            (1768, 0.0295441238874522),
            (1769, 0.1325346158749756),
            (1770, 0.036362348460972),
            (1771, 0.0888930362775058),
            (1772, 0.1511005216909173),
            (1773, 0.1740225569578286),
            (1774, 0.181814435676583),
            (1775, 0.1844360076958867),
            (1776, 0.1853168155815639),
            (1777, 0.1856126856704365),
            (1778, 0.18571207513321),
            (1779, 0.1857454650220301),
            (1780, 0.185756681470787),
            (1781, 0.1857604505721442),
            (1782, 0.1857617130388784),
            (1783, -1.607111309127523),
            (1784, -3.4875496425880166),
            (1785, -1.3227211965923305),
            (1786, -0.4872575238005176),
            (1787, -0.0961377614801349),
            (1788, 0.0885310651741068),
            (1789, 0.1529858926017705),
            (1790, 0.1747471382296157),
            (1791, 0.1820619911134124),
            (1792, 0.184519353267332),
            (1793, 0.185344816477048),
            (1794, 0.1856221003883398),
            (1795, 0.1857152427730107),
            (1796, 0.0561389030725385),
            (1797, -0.0427948529802566),
            (1798, 0.057545267787991),
            (1799, 0.1403541454616734),
            (1800, 0.1704028869763686),
            (1801, 0.1805980962819972),
            (1802, 0.1840273982453961),
            (1803, 0.1851795564739258),
            (1804, 0.1855665834344882),
            (1805, 0.185696592716987),
            (1806, 0.1857402587204534),
            (1807, 0.1857549291426783),
            (1808, 0.1857598571570931),
            (1809, -3.365688134186352),
            (1810, -2.313830028435405),
            (1811, -0.7123016214302859),
            (1812, -0.118562996879339),
            (1813, 0.0834154058417958),
            (1814, 0.1513774178324831),
            (1815, -3.3418049013197435),
            (1816, -4.328813791919775),
            (1817, -1.519519756284862),
            (1818, -0.395445519562877),
            (1819, -0.0098529515260228),
            (1820, 0.1200357166070396),
            (1821, 0.0603751726292215),
            (1822, 0.0654325060086605),
            (1823, -0.2700677190301451),
            (1824, -0.0296613843038837),
            (1825, 0.1105650611354857),
            (1826, 0.1603739551907463),
            (1827, 0.1772282548351096),
            (1828, 0.1828953875884038),
            (1829, 0.184799293647762),
            (1830, 0.1854388472573092),
            (1831, -2.2447406013527207),
            (1832, -1.4987682109213591),
            (1833, -0.4194845439142279),
            (1834, -0.0193371817849821),
            (1835, -1.6633625299236003),
            (1836, -1.0677252796589791),
            (1837, -0.2640591208376881),
            (1838, 0.0333550191991024),
            (1839, 0.1345076343649378),
            (1840, 0.1685426307197073),
            (1841, 0.1799779356154535),
            (1842, 0.1838192963195094),
            (1843, 0.1851096592809696),
            (1844, 0.1855430999305122),
            (1845, 0.1856887053352972),
            (1846, 0.0035355621131678),
            (1847, 0.0598615081906203),
            (1848, 0.1405299890709263),
            (1849, 0.1704345774563485),
            (1850, 0.1807459751025106),
            (1851, 0.1843127987017509),
            (1852, 0.179540339543076),
            (1853, 0.0158872542411766),
            (1854, -0.0141126119562986),
            (1855, 0.1129485946126033),
            (1856, 0.1222556114847754),
            (1857, -0.0448233313901343),
            (1858, 0.0862878258264031),
            (1859, 0.1535034293269437),
            (1860, 0.1767693737397144),
            (1861, 0.1162362233867286),
            (1862, -0.6237998311805185),
            (1863, -0.2585729087354761),
            (1864, 0.0379998464610089),
            (1865, 0.1429288681419851),
            (1866, 0.1744104739671799),
            (1867, 0.1846691752130716),
            (1868, 0.188148666241629),
            (1869, 0.1894123650346563),
            (1870, 0.189950840385198),
            (1871, 0.190250396871541),
            (1872, 0.1888343157402478),
            (1873, -0.0158300305583035),
            (1874, 0.1013756654566645),
            (1875, 0.1189863316340539),
            (1876, 0.1301073235870275),
            (1877, 0.1696072468545434),
            (1878, 0.1844107426763875),
            (1879, 0.1886593041289881),
            (1880, 0.152387029780733),
            (1881, 0.1480425186442423),
            (1882, 0.1874362016564929),
            (1883, -0.3245940535795368),
            (1884, -1.8150618607595548),
            (1885, -0.6420197136906102),
            (1886, -0.0852453820278208),
            (1887, -0.0250194748857913),
            (1888, 0.1350073025315394),
            (1889, 0.1858189092422608),
            (1890, 0.0703015871889916),
            (1891, -0.1023137574833239),
            (1892, 0.0776308559536416),
            (1893, 0.1864156024276895),
            (1894, 0.1928429990747818),
            (1895, 0.1930910447676056),
            (1896, 0.1931834614192998),
            (1897, 0.1932244119036768),
            (1898, 0.1932443819356002),
            (1899, 0.1932520396033143),
            (1900, 0.1932496771384894),
            (1901, 0.1931616844954455),
            (1902, 0.0905974399643504),
            (1903, -0.7087274740337839),
            (1904, -0.2643088397457709),
            (1905, 0.0775831246860811),
            (1906, 0.174940428637948),
            (1907, 0.0620316195413956),
            (1908, 0.1257742106095442),
            (1909, 0.1917775514880681),
            (1910, 0.1915901911557206),
            (1911, 0.1913996219514424),
            (1912, -0.2483084466661772),
            (1913, -0.3094316922947278),
            (1914, 0.0203984452523777),
            (1915, 0.1641375391623491),
            (1916, 0.1892217576383167),
            (1917, 0.1901831884747856),
            (1918, 0.1899763122778872),
            (1919, 0.1897601017840692),
            (1920, 0.189540706865538),
            (1921, 0.1893181118062252),
            (1922, 0.0877045766097048),
            (1923, 0.1209378339695298),
            (1924, 0.1886312109996119),
            (1925, 0.1883957416862735),
            (1926, 0.1881570617547744),
            (1927, 0.187915087386083),
            (1928, 0.1632684950596207),
            (1929, 0.0084594362993279),
            (1930, 0.1799119582279139),
            (1931, 0.1869152841968948),
            (1932, 0.0425426207362228),
            (1933, 0.1503709148960673),
            (1934, 0.1861312867254504),
            (1935, 0.1858635345120468),
            (1936, 0.185592517547358),
            (1937, 0.1853182578338796),
            (1938, 0.1850407365123296),
            (1939, 0.1847599106254542),
            (1940, 0.1844758339571321),
            (1941, 0.1841885864846894),
            (1942, 0.1838980941679814),
            (1943, 0.1836043762155363),
            (1944, 0.1833073819866889),
            (1945, 0.1830071289437376),
            (1946, 0.1827035947349408),
            (1947, 0.1823968163803705),
            (1948, 0.1820867991187164),
            (1949, 0.1817735017389544),
            (1950, 0.1814569633566329),
            (1951, 0.181137118662756),
            (1952, 0.1808140109638238),
            (1953, 0.1804876751844325),
            (1954, 0.1801580463648328),
            (1955, 0.1798251692085081),
            (1956, 0.1794890063461402),
            (1957, 0.1791495207576567),
            (1958, 0.1788067540033275),
            (1959, 0.1784607567238176),
            (1960, 0.1781114643086233),
            (1961, 0.1748425912224242),
            (1962, 0.01887847791617),
            (1963, -0.7158139715324602),
            (1964, -0.6203003960549346),
            (1965, -0.2927293197139612),
            (1966, 0.1169096523076781),
            (1967, -0.076337447099339),
            (1968, 0.0011209927611538),
            (1969, 0.0748592184968778),
            (1970, 0.07891007914399),
            (1971, -0.0321334103941431),
            (1972, 0.0491196539365241),
            (1973, 0.1552288305825108),
            (1974, 0.1027906612139681),
            (1975, -0.2049690165444722),
            (1976, 0.0427959312797078),
            (1977, 0.1284540133197346),
            (1978, 0.1506635484397897),
            (1979, 0.1473114304822424),
            (1980, 0.109190156973947),
            (1981, 0.0757372745424995),
            (1982, -0.1564158400874098),
            (1983, -0.6775945263802521),
            (1984, -0.2289078353791943),
            (1985, -0.0117157005592694),
            (1986, -0.00014658150072006793),
            (1987, 0.0621697560996303),
            (1988, 0.1102479335964212),
            (1989, 0.1426154615469762),
            (1990, 0.1407953117155024),
            (1991, -0.4148185776434353),
            (1992, -1.6835767484157795),
            (1993, -0.8170844043492784),
            (1994, -0.0813850082344821),
            (1995, 0.0853077211063841),
            (1996, 0.1456922256034353),
            (1997, 0.1669024887374156),
            (1998, 0.1710925825750941),
            (1999, 0.1732418502793201),
            (2000, 0.1745824169479796),
            (2001, 0.170843036204625),
            (2002, 0.1765222575627753),
            (2003, 0.165150043379564),
            (2004, 0.1719032893302405),
            (2005, 0.1498078532163539),
            (2006, 0.1245541128442177),
            (2007, 0.1214193886258194),
            (2008, 0.133277034444783),
            (2009, 0.1066842123978326),
            (2010, 0.1379875550624469),
            (2011, 0.1090569133516887),
            (2012, 0.1386751812529304),
            (2013, 0.157671543128837),
            (2014, 0.1397783633433768),
            (2015, 0.1258005270090391),
            (2016, 0.1118226906747014),
            (2017, 0.0978448543403637),
            (2018, 0.083867018006026),
            (2019, 0.0698891816716884),
            (2020, 0.0559113453373507),
            (2021, 0.041933509003013),
            (2022, 0.0279556726686753),
            (2023, 0.0139778363343376),
            (2024, 0.0),
            (2025, 0.0),
            (2026, 0.0),
            (2027, 0.0),
            (2028, 0.0),
            (2029, 0.0),
            (2030, 0.0),
            (2031, 0.0),
            (2032, 0.0),
            (2033, 0.0),
            (2034, 0.0),
            (2035, 0.0),
            (2036, 0.0),
            (2037, 0.0),
            (2038, 0.0),
            (2039, 0.0),
            (2040, 0.0),
            (2041, 0.0),
            (2042, 0.0),
            (2043, 0.0),
            (2044, 0.0),
            (2045, 0.0),
            (2046, 0.0),
            (2047, 0.0),
            (2048, 0.0),
            (2049, 0.0),
            (2050, 0.0),
            (2051, 0.0),
            (2052, 0.0),
            (2053, 0.0),
            (2054, 0.0),
            (2055, 0.0),
            (2056, 0.0),
            (2057, 0.0),
            (2058, 0.0),
            (2059, 0.0),
            (2060, 0.0),
            (2061, 0.0),
            (2062, 0.0),
            (2063, 0.0),
            (2064, 0.0),
            (2065, 0.0),
            (2066, 0.0),
            (2067, 0.0),
            (2068, 0.0),
            (2069, 0.0),
            (2070, 0.0),
            (2071, 0.0),
            (2072, 0.0),
            (2073, 0.0),
            (2074, 0.0),
            (2075, 0.0),
            (2076, 0.0),
            (2077, 0.0),
            (2078, 0.0),
            (2079, 0.0),
            (2080, 0.0),
            (2081, 0.0),
            (2082, 0.0),
            (2083, 0.0),
            (2084, 0.0),
            (2085, 0.0),
            (2086, 0.0),
            (2087, 0.0),
            (2088, 0.0),
            (2089, 0.0),
            (2090, 0.0),
            (2091, 0.0),
            (2092, 0.0),
            (2093, 0.0),
            (2094, 0.0),
            (2095, 0.0),
            (2096, 0.0),
            (2097, 0.0),
            (2098, 0.0),
            (2099, 0.0),
            (2100, 0.0),
            (2101, 0.0),
            (2102, 0.0),
            (2103, 0.0),
            (2104, 0.0),
            (2105, 0.0),
            (2106, 0.0),
            (2107, 0.0),
            (2108, 0.0),
            (2109, 0.0),
            (2110, 0.0),
            (2111, 0.0),
            (2112, 0.0),
            (2113, 0.0),
            (2114, 0.0),
            (2115, 0.0),
            (2116, 0.0),
            (2117, 0.0),
            (2118, 0.0),
            (2119, 0.0),
            (2120, 0.0),
            (2121, 0.0),
            (2122, 0.0),
            (2123, 0.0),
            (2124, 0.0),
            (2125, 0.0),
            (2126, 0.0),
            (2127, 0.0),
            (2128, 0.0),
            (2129, 0.0),
            (2130, 0.0),
            (2131, 0.0),
            (2132, 0.0),
            (2133, 0.0),
            (2134, 0.0),
            (2135, 0.0),
            (2136, 0.0),
            (2137, 0.0),
            (2138, 0.0),
            (2139, 0.0),
            (2140, 0.0),
            (2141, 0.0),
            (2142, 0.0),
            (2143, 0.0),
            (2144, 0.0),
            (2145, 0.0),
            (2146, 0.0),
            (2147, 0.0),
            (2148, 0.0),
            (2149, 0.0),
            (2150, 0.0),
            (2151, 0.0),
            (2152, 0.0),
            (2153, 0.0),
            (2154, 0.0),
            (2155, 0.0),
            (2156, 0.0),
            (2157, 0.0),
            (2158, 0.0),
            (2159, 0.0),
            (2160, 0.0),
            (2161, 0.0),
            (2162, 0.0),
            (2163, 0.0),
            (2164, 0.0),
            (2165, 0.0),
            (2166, 0.0),
            (2167, 0.0),
            (2168, 0.0),
            (2169, 0.0),
            (2170, 0.0),
            (2171, 0.0),
            (2172, 0.0),
            (2173, 0.0),
            (2174, 0.0),
            (2175, 0.0),
            (2176, 0.0),
            (2177, 0.0),
            (2178, 0.0),
            (2179, 0.0),
            (2180, 0.0),
            (2181, 0.0),
            (2182, 0.0),
            (2183, 0.0),
            (2184, 0.0),
            (2185, 0.0),
            (2186, 0.0),
            (2187, 0.0),
            (2188, 0.0),
            (2189, 0.0),
            (2190, 0.0),
            (2191, 0.0),
            (2192, 0.0),
            (2193, 0.0),
            (2194, 0.0),
            (2195, 0.0),
            (2196, 0.0),
            (2197, 0.0),
            (2198, 0.0),
            (2199, 0.0),
            (2200, 0.0),
            (2201, 0.0),
            (2202, 0.0),
            (2203, 0.0),
            (2204, 0.0),
            (2205, 0.0),
            (2206, 0.0),
            (2207, 0.0),
            (2208, 0.0),
            (2209, 0.0),
            (2210, 0.0),
            (2211, 0.0),
            (2212, 0.0),
            (2213, 0.0),
            (2214, 0.0),
            (2215, 0.0),
            (2216, 0.0),
            (2217, 0.0),
            (2218, 0.0),
            (2219, 0.0),
            (2220, 0.0),
            (2221, 0.0),
            (2222, 0.0),
            (2223, 0.0),
            (2224, 0.0),
            (2225, 0.0),
            (2226, 0.0),
            (2227, 0.0),
            (2228, 0.0),
            (2229, 0.0),
            (2230, 0.0),
            (2231, 0.0),
            (2232, 0.0),
            (2233, 0.0),
            (2234, 0.0),
            (2235, 0.0),
            (2236, 0.0),
            (2237, 0.0),
            (2238, 0.0),
            (2239, 0.0),
            (2240, 0.0),
            (2241, 0.0),
            (2242, 0.0),
            (2243, 0.0),
            (2244, 0.0),
            (2245, 0.0),
            (2246, 0.0),
            (2247, 0.0),
            (2248, 0.0),
            (2249, 0.0),
            (2250, 0.0),
            (2251, 0.0),
            (2252, 0.0),
            (2253, 0.0),
            (2254, 0.0),
            (2255, 0.0),
            (2256, 0.0),
            (2257, 0.0),
            (2258, 0.0),
            (2259, 0.0),
            (2260, 0.0),
            (2261, 0.0),
            (2262, 0.0),
            (2263, 0.0),
            (2264, 0.0),
            (2265, 0.0),
            (2266, 0.0),
            (2267, 0.0),
            (2268, 0.0),
            (2269, 0.0),
            (2270, 0.0),
            (2271, 0.0),
            (2272, 0.0),
            (2273, 0.0),
            (2274, 0.0),
            (2275, 0.0),
            (2276, 0.0),
            (2277, 0.0),
            (2278, 0.0),
            (2279, 0.0),
            (2280, 0.0),
            (2281, 0.0),
            (2282, 0.0),
            (2283, 0.0),
            (2284, 0.0),
            (2285, 0.0),
            (2286, 0.0),
            (2287, 0.0),
            (2288, 0.0),
            (2289, 0.0),
            (2290, 0.0),
            (2291, 0.0),
            (2292, 0.0),
            (2293, 0.0),
            (2294, 0.0),
            (2295, 0.0),
            (2296, 0.0),
            (2297, 0.0),
            (2298, 0.0),
            (2299, 0.0),
            (2300, 0.0),
        ]
    },
    "temperature": {"S": 3.0, "alpha": 1.0, "diff": 2.38, "qco2": 3.75, "volscl": 1.0},
}
