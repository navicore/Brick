from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.collection import Collection
from rdflib.extras.infixowl import Restriction

BRICK = Namespace("https://brickschema.org/schema/1.0.3/Brick#")
BRICKTAG = Namespace("https://brickschema.org/schema/1.0.3/BrickTag#")
BLDG = Namespace("https://brickschema.org/schema/1.0.3/ExampleBuilding#")
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
A = RDF.type

point_definitions = {
    "Setpoint": {
        "tagvalues": [[BRICK.hasTag, BRICKTAG.Setpoint]],
        "subclasses": {
            "Temperature_Setpoint": {
                "tagvalues": [[BRICK.hasTag, BRICK["Temperature"]], [BRICK.hasTag, BRICK["Setpoint"]]],
                "subclasses": {
                    "Air_Temperature_Setpoint": {
                        "tagvalues": [[BRICK.hasTag, BRICK["Air"]], [BRICK.hasTag, BRICK["Temperature"]], [BRICK.hasTag, BRICK["Setpoint"]]],
                        "subclasses": {
                            "Discharge_Air_Temperature_Setpoint": {
                                "tagvalues": [[BRICK.hasTag, BRICK["Discharge"]], [BRICK.hasTag, BRICK["Air"]], [BRICK.hasTag, BRICK["Temperature"]], [BRICK.hasTag, BRICK["Setpoint"]]],
                                "subclasses": {
                                    "Discharge_Air_Temperature_Heating_Setpoint": {
                                        OWL.equivalentClass: "Minimum_Discharge_Air_Temperature_Setpoint",
                                    },
                                    "Discharge_Air_Temperature_Cooling_Setpoint": {
                                        OWL.equivalentClass: "Maximum_Discharge_Air_Temperature_Setpoint",
                                    },
                                },
                            },
                            "Mixed_Air_Temperature_Setpoint": {
                                "tagvalues": [[BRICK.hasTag, BRICK["Mixed"]], [BRICK.hasTag, BRICK["Air"]], [BRICK.hasTag, BRICK["Temperature"]], [BRICK.hasTag, BRICK["Setpoint"]]],
                            },
                            "Room_Air_Temperature_Setpoint": {},
                            "Outside_Air_Temperature_Setpoint": {
                                "tagvalues": [[BRICK.hasTag, BRICK["Outside"]], [BRICK.hasTag, BRICK["Air"]], [BRICK.hasTag, BRICK["Temperature"]], [BRICK.hasTag, BRICK["Setpoint"]]],
                                "subclasses": {
                                    "Low_Outside_Air_Temperature_Enable_Setpoint": {},
                                    "Open_Heating_Valve_Outside_Air_Temperature_Setpoint": {},
                                    "Outside_Air_Lockout_Temperature_Setpoint": {},
                                },
                            },
                        },
                    },
                    "Water_Temperature_Setpoint": {
                        "tagvalues": [
                            [BRICK.hasTag, BRICKTAG.Setpoint],
                            [BRICK.hasTag, BRICKTAG.Temperature],
                            [BRICK.hasTag, BRICKTAG.Water],
                        ],
                        "subclasses": {
                            "Entering_Water_Temperature_Setpoint": {
                                "tagvalues": [
                                    [BRICK.hasTag, BRICKTAG.Entering],
                                    [BRICK.hasTag, BRICKTAG.Setpoint],
                                    [BRICK.hasTag, BRICKTAG.Temperature],
                                    [BRICK.hasTag, BRICKTAG.Water],
                                ],
                            },
                            "Leaving_Water_Temperature_Setpoint": {
                                "tagvalues": [
                                    [BRICK.hasTag, BRICKTAG.Entering],
                                    [BRICK.hasTag, BRICKTAG.Setpoint],
                                    [BRICK.hasTag, BRICKTAG.Temperature],
                                    [BRICK.hasTag, BRICKTAG.Water],
                                ],
                            },
                        },
                    },
                },
            },
            "CO2_Setpoint": {
                "tagvalues": [
                    [BRICK.hasTag, BRICKTAG.Setpoint],
                    [BRICK.hasTag, BRICKTAG.CO2],
                ],
                "subclasses": {
                    "Return_Air_CO2_Setpoint": {
                        "tagvalues": [
                            [BRICK.hasTag, BRICKTAG.Setpoint],
                            [BRICK.hasTag, BRICKTAG.Return],
                            [BRICK.hasTag, BRICKTAG.CO2],
                        ],
                        "subclasses": {
                            "Max_Return_Air_CO2_Setpoint": {
                            }
                        },
                    }
                },
            },
        },
    },
    "Sensor": {
        "tagvalues": [
            [BRICK.hasTag, BRICKTAG.Sensor]
        ],
        "subclasses": {
            "CO2_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, BRICKTAG.Sensor],
                    [BRICK.hasTag, BRICKTAG.CO2],
                ],
                "subclasses": {
                    "CO2_Differential_Sensor": {},
                    "CO2_Level_Sensor": {},
                },
            },
            "Temperature_Sensor": {
                "tagvalues": [
                    [BRICK.hasTag, BRICKTAG.Sensor],
                    [BRICK.hasTag, BRICKTAG.Temperature],
                ],
                "subclasses": {
                    "Zone_Temperature_Sensor": {
                        "subclasses": {
                            "Average_Zone_Temperature_Sensor": {},
                            "Highest_Zone_Temperature_Sensor": {
                                OWL.equivalentClass: "Warmest_Zone_Temperature_Sensor"
                            },
                            "Lowest_Zone_Temperature_Sensor": {
                                OWL.equivalentClass: "Coldest_Zone_Temperature_Sensor"
                            },
                        },
                    },
                    "Air_Temperature_Sensor": {
                        "subclasses": {
                            "Discharge_Air_Temperature_Sensor": {
                                OWL.equivalentClass: "Supply_Air_Temperature_Sensor",
                                "subclasses": {
                                    "Cooling_Coil_Discharge_Air_Temperature_Sensor": {},
                                    "Heat_Wheel_Discharge_Air_Temperature_Sensor": {},
                                    "Preheat_Discharge_Air_Temperature_Sensor": {},
                                },
                            },
                            "Zone_Air_Temperature_Sensor": {},
                            "Exhaust_Air_Temperature_Sensor": {},
                            "Mixed_Air_Temperature_Sensor": {},
                            "Return_Air_Temperature_Sensor": {},
                            "Outside_Air_Temperature_Sensor": {
                                "subclasses": {
                                    "Outside_Air_Lockout_Temperature_Differential_Sensor": {
                                        "subclasses": {
                                            "Low_Outside_Air_Lockout_Temperature_Differential_Sensor": {},
                                            "High_Outside_Air_Lockout_Temperature_Differential_Sensor": {},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "Water_Temperature_Sensor": {
                        "subclasses": {
                            "Chilled_Water_Supply_Temperature_Sensor": {
                                OWL.equivalentClass: "Chilled_Water_Discharge_Temperature_Sensor",
                            },
                            "Heat_Exchanger_Supply_Water_Temperature_Sensor": {},
                            "Hot_Water_Supply_Temperature_Sensor": {
                                "subclasses": {
                                    "Domestic_Hot_Water_Supply_Temperature_Sensor": {},
                                    "High_Temperature_Hot_Water_Supply_Temperature_Sensor": {},
                                    "Medium_Temperature_Hot_Water_Supply_Temperature_Sensor": {},
                                },
                            },
                            "Chilled_Water_Temperature_Sensor": {
                                "subclasses": {
                                    "Chilled_Water_Differential_Temperature_Sensor": {},
                                },
                            },
                            "Entering_Water_Temperature_Sensor": {
                                "subclasses": {
                                    "Hot_Water_Coil_Entering_Temperature_Sensor": {},
                                    "Ice_Tank_Entering_Water_Temperature_Sensor": {},
                                    "PreHeat_Coil_Entering_Air_Temperature_Sensor": {},
                                },
                            },
                            "Leaving_Water_Temperature_Sensor": {
                                "subclasses": {
                                    "Ice_Tank_Leaving_Water_Temperature_Sensor": {},
                                    "PreHeat_Coil_Leaving_Air_Temperature_Sensor": {},
                                },
                            },
                            "Return_Water_Temperature_Sensor": {
                                "subclasses": {
                                    "Hot_Water_Return_Temperature_Sensor": {},
                                    "Chilled_Water_Return_Temperature_Sensor": {},
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
