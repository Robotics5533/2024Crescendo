from autons.autons.OneTaxi import OneTaxi
from autons.autons.OneTaxiLeft import OneTaxiLeft
from autons.autons.OneTaxiRight import OneTaxiRight
from autons.autons.ThreePieceLeft import ThreePieceLeft
from autons.autons.ThreePieceRight import ThreePieceRight
from autons.autons.TwoPiece import TwoPiece
from subsystems.index import SubSystems

AutonList = ["TwoPiece", "ThreePieceLeft", "ThreePieceRight", "OneTaxi", "OneTaxiPositionLeft", "OneTaxiPositionRight"]

def create_auton(subsystems: SubSystems, type: str, timer):
        match type:
            case "TwoPiece":
                return TwoPiece(subsystems, timer)
            case "ThreePieceLeft":
                  return ThreePieceLeft(subsystems, timer)
            case "ThreePieceRight":
                  return ThreePieceRight(subsystems, timer)
            case "OneTaxi":
                return OneTaxi(subsystems, timer)
            case "OneTaxiPositionLeft":
                  return OneTaxiLeft(subsystems, timer)
            case "OneTaxiPositionRight":
                  return OneTaxiRight(subsystems, timer)
                  