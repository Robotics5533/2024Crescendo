from autons.autons.OneTaxi import OneTaxi
from autons.autons.OneTaxiLeft import OneTaxiLeft
from autons.autons.OneTaxiRight import OneTaxiRight
from autons.autons.ThreePieceLeftUnstable import ThreePieceLeftUnstable
from autons.autons.ThreePieceRightUnstable import ThreePieceRightUnstable
from autons.autons.ThreePieceLeft import ThreePieceLeft
from autons.autons.ThreePieceRight import ThreePieceRight
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems

AutonList = ["TwoPiece", "OneTaxi", "OneTaxiPositionLeft", "OneTaxiPositionRight", "ThreePieceRightUnstable", "ThreePieceLeftUnstable"]

def create_auton(subsystems: SubSystems, type: str, timer):
        match type:
            case "TwoPiece":
                return TwoPiece(subsystems, timer)
            case "OneTaxi":
                return OneTaxi(subsystems, timer)
            case "OneTaxiPositionLeft":
                  return OneTaxiLeft(subsystems, timer)
            case "OneTaxiPositionRight":
                  return OneTaxiRight(subsystems, timer)
            case "ThreePieceRightUnstable":
              return ThreePieceRightUnstable(subsystems, timer)
            case "ThreePieceLeftUnstable":
              return ThreePieceLeftUnstable(subsystems, timer)
                  