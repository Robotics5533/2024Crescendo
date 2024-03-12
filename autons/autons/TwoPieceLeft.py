from autons.auton2 import Auton

from autons.autons.TwoPieceRight import TwoPieceRight
from subsystems.index import SubSystems


class TwoPieceLeft(Auton):
    def __init__(self, subsystems: SubSystems, timer):
        super().__init__(subsystems, timer)
        self.subsystems = subsystems
        self.two_piece_right = TwoPieceRight(subsystems, timer, self.tasks)
        self.two_piece_right.invert(z = True)

    def run(self):
        self.two_piece_right.run()

