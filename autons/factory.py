from autons.autons.FourPiece import FourPiece
from autons.autons.LeftPiece import LeftPiece
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems

AutonList = ["TwoPiece", "FourPiece", "LeftPiece"]

def create_auton(subsystems: SubSystems, type: str, timer):
        match type:
            case "TwoPiece":
                return TwoPiece(subsystems, timer)
            case "FourPiece":
                  return FourPiece(subsystems, timer)
            case "LeftPiece":
                  return LeftPiece(subsystems, timer)