from units import *
columnSections = {
    "NBC_205_1994": {
        "material":{"Confined_Concrete":{"MaterialTag":1,
                                         "fpc":-18.62*MPa,
                                         "epsc0":-0.004,
                                         "fpcu":-0.2*18.62*MPa,
                                         "epsU":-0.01,
                                         "lambda":0.1,
                                         },
                    "Unconfined_Concrete":{"MaterialTag":2,
                                         "fpc":-15.6*MPa,
                                         "epsc0":-0.002,
                                         "fpcu":-0.2*15.6*MPa,
                                         "epsU":-0.004,
                                         "lambda":0.1,
                                         },
                        "SteelRebar":{"MaterialTag":3,
                                         "E":2e5*MPa,
                                         "b":0.2/100,
                                         "fy":415*1.17*MPa, #set
                                         }
# number of bars and their layout to be specified
},
"cover":{"cover": 40*mm},
"sectionDimensions":{"width": 230*mm,
                      "depth": 230*mm}
},




"NBC_205_2012": {
        "material":{"Confined_Concrete":{"MaterialTag":1,
                                         "fpc":-26.01*MPa,
                                         "epsc0":-0.002,
                                         "fpcu":-0.2*26.01*MPa,
                                         "epsU":-0.01,
                                         "lambda":0.1,
                                         },
                    "Unconfined_Concrete":{"MaterialTag":2,
                                         "fpc":-20.8*MPa,
                                         "epsc0":-0.0047,
                                         "fpcu":-0.2*20.8*MPa,
                                         "epsU":-0.004,
                                         "lambda":0.1,
                                         },
                        "SteelRebar":{"MaterialTag":3,
                                         "E":2e5*MPa,
                                         "b":0.2/100,
                                         "fy":500*1.17*MPa, # set
                                         }
},
"cover":{"cover": 40*mm},
"sectionDimensions":{"width": 300*mm,
                      "depth": 300*mm}
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
"cover":{"cover": 40*mm},
"sectionDimensions":{"width": 350*mm,
                      "depth": 350*mm}
}
# beam concrete material tag should start from 4