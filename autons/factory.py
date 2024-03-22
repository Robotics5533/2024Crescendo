from autons.autons.FourPieceBlue import FourPieceBlue
from autons.autons.FourPieceRed import FourPieceRed
from autons.autons.OnePiece import OnePiece
from autons.autons.OneTaxi import OneTaxi
from autons.autons.OneTaxiLeft import OneTaxiLeft
from autons.autons.OneTaxiRight import OneTaxiRight
from autons.autons.ThreePieceBlueAmp import ThreePieceBlueAmp
from autons.autons.ThreePieceBlueStage import ThreePieceBlueStage
from autons.autons.TwoPiece import TwoPiece
from autons.autons.TwoPieceLeft import TwoPieceLeft
from autons.autons.TwoPieceRight import TwoPieceRight
from subsystems.index import SubSystems

AutonList = [
     "OnePiece",
     "OneTaxi",
     "OneTaxiLeft",
     "OneTaxiRight",
     "TwoPiece",
     "TwoPieceLeft",
     "TwoPieceRight",
     "ThreePieceBlueStage",
     "ThreePieceBlueAmp",
     "ThreePieceRedStage",
     "ThreePieceRedAmp",
     "FourPieceRed",
     "FourPieceBlue"
]

def create_auton(subsystems: SubSystems, auton_name: str, timer):
        match auton_name:
            case "OneTaxi":
                return OneTaxi(subsystems, timer)
            case "OneTaxiLeft":
                  return OneTaxiLeft(subsystems, timer)
            case "OneTaxiRight":
                  return OneTaxiRight(subsystems, timer)
            case "TwoPiece":
                  return TwoPiece(subsystems, timer)
            case "TwoPieceLeft":
                  return TwoPieceLeft(subsystems, timer)
            case "TwoPieceRight":
                  return TwoPieceRight(subsystems, timer)
            case "ThreePieceBlueStage":
                    return ThreePieceBlueStage(subsystems, timer)
            case "ThreePieceBlueAmp":
                    return ThreePieceBlueAmp(subsystems, timer)
            case "ThreePieceRedStage":
                    return ThreePieceBlueAmp(subsystems, timer)
            case "ThreePieceRedAmp":
                    return ThreePieceBlueStage(subsystems, timer)
            case "FourPieceRed":
                      return FourPieceRed(subsystems, timer)
            case "FourPieceBlue":
                      return FourPieceBlue(subsystems, timer)
               
            case "OnePiece":
                      return OnePiece(subsystems, timer)
                  