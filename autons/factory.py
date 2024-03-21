
from autons.autons.OneTaxi import OneTaxi
from autons.autons.OneTaxiLeft import OneTaxiLeft
from autons.autons.OneTaxiRight import OneTaxiRight
from subsystems.index import SubSystems

AutonList = [
     "OneTaxi",
     "OneTaxiLeft",
     "OneTaxiRight"
]

def create_auton(subsystems: SubSystems, auton_name: str, timer):
        match auton_name:
            case "OneTaxi":
                return OneTaxi(subsystems, timer)
            case "OneTaxiLeft":
                  return OneTaxiLeft(subsystems, timer)
            case "OneTaxiRight":
                    return OneTaxiRight(subsystems, timer)
                  