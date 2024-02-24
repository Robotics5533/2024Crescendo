from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems

AutonList = ["TwoPiece"]

def create_auton(subsystems: SubSystems, type: str):
        match type:
            case "TwoPiece":
                return TwoPiece(subsystems)