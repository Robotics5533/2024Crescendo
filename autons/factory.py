from autons.autons.OneTaxi import OneTaxi
from autons.autons.OneTaxiLeft import OneTaxiLeft
from autons.autons.OneTaxiRight import OneTaxiRight
from autons.autons.ThreePiece import ThreePiece
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems

AutonList = ["TwoPiece", "ThreePiece", "OneTaxi", "OneTaxiPositionLeft", "OneTaxiPositionRight", "Autism"]

def create_auton(subsystems: SubSystems, type: str, timer):
        match type:
            case "TwoPiece":
                return TwoPiece(subsystems, timer)
            case "ThreePiece":
                  return ThreePiece(subsystems, timer)
            case "OneTaxi":
                return OneTaxi(subsystems, timer)
            case "OneTaxiPositionLeft":
                  return OneTaxiLeft(subsystems, timer)
            case "OneTaxiPositionRight":
                  return OneTaxiRight(subsystems, timer)
            case "Autism":
                  return ThreePiece(subsystems, timer)
                  
                  