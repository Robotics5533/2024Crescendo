from autons.autons.FourPiece import FourPiece
from autons.autons.FourPiece2 import FourPiece2
from autons.autons.LeftPiece import LeftPiece
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems

AutonList = ["TwoPiece", "FourPiece", "LeftPiece", "FourPiece2"]

def create_auton(subsystems: SubSystems, type: str, timer):
        match type:
            case "TwoPiece":
                return TwoPiece(subsystems, timer)
            case "FourPiece":
                  return FourPiece(subsystems, timer)
            case "FourPiece2":
                  return FourPiece2(subsystems, timer)
            case "LeftPiece":
                  return LeftPiece(subsystems, timer)