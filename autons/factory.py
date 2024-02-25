from autons.autons.OneTaxi import OneTaxi
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems

AutonList = ["TwoPiece", "OneTaxi"]

def create_auton(subsystems: SubSystems, type: str, timer):
        match type:
            case "TwoPiece":
                return TwoPiece(subsystems, timer)
            case "OneTaxi":
                return OneTaxi(subsystems, timer)