
from autons.autons.OneTaxi import OneTaxi
from autons.autons.OneTaxiLeft import OneTaxiLeft
from autons.autons.OneTaxiRight import OneTaxiRight
from autons.autons.ThreePieceBlueStage import ThreePieceBlueStage
from autons.autons.TwoPiece import TwoPiece
from autons.autons.TwoPieceLeft import TwoPieceLeft
from autons.autons.TwoPieceRight import TwoPieceRight
from subsystems.index import SubSystems

AutonList = [
     "OneTaxi",
     "OneTaxiLeft",
     "OneTaxiRight",
     "TwoPiece",
     "TwoPieceLeft",
     "TwoPieceRight",
     "ThreePieceBlueStage"
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
               
                  