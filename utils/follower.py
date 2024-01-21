from utils.context import Context


class Follower:
    def __init__(self, ctx: Context):
        self.ctx = ctx
        self.command = 0
        self.commands=[
                (self.ctx.rotate, -272.7367008673047),
                (self.ctx.move, (490, 210)),
                (self.ctx.rotate, 271.9231976564468),
                (self.ctx.move, (248, 466)),
            ]
    def update(self):
        if self.ctx.next():
            self.command += 1
            (f, p) = self.commands[self.command]
            f(p)


