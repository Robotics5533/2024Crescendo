from utils.context import Context
from utils.math.Vector import Vector


class Follower:
    def __init__(self, ctx: Context):
        self.ctx = ctx
        self.command = 0
        self.commands=[
                # (self.ctx.rotate, -272.7367008673047),
                (self.ctx.move, Vector(0, 210, 0)),
                # (self.ctx.rotate, 271.9231976564468),
                (self.ctx.move, Vector(0, -466, 0)),
            ]
    def update(self):
        if self.ctx.next():
            self.command += 1
            if self.command >= len(self.commands): 
                return
            (f, p) = self.commands[self.command]
            f(p)


