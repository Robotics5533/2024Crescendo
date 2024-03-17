from autons.autons.FourPieceUnstable import FourPieceUnstable
from autons.autons.OnePieceNoTaxi import OnePieceNoTaxi
from autons.autons.OneTaxi import OneTaxi
from autons.autons.OneTaxiLeft import OneTaxiLeft
from autons.autons.OneTaxiRight import OneTaxiRight
from autons.autons.ThreePieceFast import ThreePieceFast
from autons.autons.ThreePieceLeftUnstable import ThreePieceLeftUnstable
from autons.autons.ThreePieceRightUnstable import ThreePieceRightUnstable
from autons.autons.ThreePieceLeft import ThreePieceLeft
from autons.autons.ThreePieceRight import ThreePieceRight
from autons.autons.TwoPiece import TwoPiece
from autons.autons.TwoPieceLeft import TwoPieceLeft
from autons.autons.TwoPieceRight import TwoPieceRight
from subsystems.index import SubSystems

AutonList = ["FourPiece", "ThreePieceFast", "TwoPiece", "OnePieceNoTaxi", "OneTaxi", "OneTaxiPositionLeft", "OneTaxiPositionRight", "ThreePieceRightUnstable", "ThreePieceLeftUnstable","TwoPieceRight", "TwoPieceLeft"]

def create_auton(subsystems: SubSystems, type: str, timer):
        match type:
            case "TwoPiece":
                return TwoPiece(subsystems, timer)
            case "OneTaxi":
                return OneTaxi(subsystems, timer)
            case "OnePieceNoTaxi":
                  return OnePieceNoTaxi(subsystems, timer)
            case "OneTaxiPositionLeft":
                  return OneTaxiLeft(subsystems, timer)
            case "OneTaxiPositionRight":
                  return OneTaxiRight(subsystems, timer)
            case "ThreePieceRightUnstable":
              return ThreePieceRightUnstable(subsystems, timer)
            case "ThreePieceLeftUnstable":
              return ThreePieceLeftUnstable(subsystems, timer)
            case "TwoPieceRight":
                  return TwoPieceRight(subsystems,timer)
            case "TwoPieceLeft":
                  return TwoPieceLeft(subsystems,timer)
            case "ThreePieceFast":
                  return ThreePieceFast(subsystems, timer)
            case "FourPiece":
                  return FourPieceUnstable(subsystems, timer)
                  