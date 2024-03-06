from autons.autons.OneTaxi import OneTaxi
from autons.autons.ThreePiece import ThreePiece
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems

AutonList = ["TwoPiece", "ThreePiece", "OneTaxi"]

def create_auton(subsystems: SubSystems, type: str, timer):
        match type:
            case "TwoPiece":
                return TwoPiece(subsystems, timer)
            case "ThreePiece":
                  return ThreePiece(subsystems, timer)
            case "OneTaxi":
                return OneTaxi(subsystems, timer)