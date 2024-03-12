from autons.auton2 import Auton
from autons.autons.ThreePieceRightUnstable import ThreePieceRightUnstable
from subsystems.index import SubSystems
class ThreePieceLeftUnstable(Auton):
    def __init__(self, subsystems: SubSystems, timer):
        super().__init__(subsystems, timer)
        self.subsystems = subsystems
        self.three_piece_right = ThreePieceRightUnstable(subsystems, timer, self.tasks)
        self.three_piece_right.invert(x = True)


    def run(self):
      self.three_piece_right.run()

