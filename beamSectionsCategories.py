from units import *


beamSections = {
    "NBC_205_1994": {
        "material":{"Confined_Concrete":{"MaterialTag":4,
                                         "fpc":-18.62*MPa,
                                         "epsc0":-0.004,
                                         "fpcu":-0.2*18.62*MPa,
                                         "epsU":-0.01,
                                         "lambda":0.1,
                                         },
                    "Unconfined_Concrete":{"MaterialTag":5,
                                         "fpc":-15.6*MPa,
                                         "epsc0":-0.002,
                                         "fpcu":-0.2*15.6*MPa,
                                         "epsU":-0.004,
                                         "lambda":0.1,
                                         },
                        "SteelRebar":{"MaterialTag":6,
                                         "E":2e5*MPa,
                                         "b":0.2/100,
                                         "fy":415*1.17*MPa, #set
                                         }
# number of bars and their layout to be specified
},
"sectionDimensions":{"width": 230*mm,
                      "depth": 325*mm}
},




"NBC_205_2012": {
        "material":{"Confined_Concrete":{"MaterialTag":4,
                                         "fpc":-26.01*MPa,
                                         "epsc0":-0.002,
                                         "fpcu":-0.2*26.01*MPa,
                                         "epsU":-0.01,
                                         "lambda":0.1,
                                         },
                    "Unconfined_Concrete":{"MaterialTag":5,
                                         "fpc":-20.8*MPa,
                                         "epsc0":-0.0047,
                                         "fpcu":-0.2*20.8*MPa,
                                         "epsU":-0.004,
                                         "lambda":0.1,
                                         },
                        "SteelRebar":{"MaterialTag":6,
                                         "E":2e5*MPa,
                                         "b":0.2/100,
                                         "fy":500*1.17*MPa, # set
                                         }
},
"sectionDimensions":{"width": 230*mm,
                      "depth": 355*mm}
},
"NBC_205_2024": {
        "material":{"Confined_Concrete":{"MaterialTag":4,
                                         "fpc":-33.91*MPa, #to be set later
                                         "epsc0":-0.009,
                                         "fpcu":-0.2*33.91*MPa,
                                         "epsU":-0.01,
                                         "lambda":0.1,
                                         },
                    "Unconfined_Concrete":{"MaterialTag":5,
                                         "fpc":-20.8*MPa, #to be set later
                                         "epsc0":-0.002, #to be set later
                                         "fpcu":-0.2*20.8*MPa, #to be set later
                                         "epsU":-0.004, #to be set later
                                         "lambda":0.1, #to be set later
                                         },
                        "SteelRebar":{"MaterialTag":6,
                                         "E":2e5*MPa,
                                         "b":0.2/100,
                                         "fy":500*1.17*MPa, #to be set later
                                         }
}
},
"sectionDimensions":{"width": 250*mm,
                      "depth": 380*mm}
}
