import ntcore


class Limelight:
    def __init__(self):
        self.ntinst = ntcore.NetworkTableInstance.getDefault()
        self.limelight_ntable = self.ntinst.getTable('limelight')


    def get_limelight_arg(self, channel: str, default_value: int = 0):
        return self.limelight_ntable.getNumber(channel, default_value)

    def getoffset(self):
        if not self.get_limelight_arg("tv", 0):
            return [0, 0, 0]
        else:
            #            return [self.get_limelight_arg("tx"), self.get_limelight_arg("ty"), self.apply_turning_error()]
            #            return [self.get_limelight_arg("tx")/27, self.AreaToDifference(self.get_limelight_arg('ta'))/50, 0/100] # division values come from limelight docs page 12
            # division values come from limelight docs page 12
            return [(self.get_limelight_arg("tx")/27), 1-(self.get_limelight_arg('ta'))/100, (self.get_limelight_arg("tx")/27)]
        
        
        
        
    def getError(self,close_enough_y = .7):
        x, y, z = self.getoffset()
        print(y)
        ret_y = -y*(1-abs(x))
        if y < close_enough_y:
            ret_y = 0
            
        return [x, ret_y, z]