from math import floor

def fmod(x, b):
    return x - b * floor(x / b)

def clamp(x, mi, ma):
    return max(mi, min(x,ma))
    
def linear_remap(x, si, ei, sf, ef):
    slope = (sf - ef) / (si - ei)
    y_intercept = sf - (si * slope)
    return slope * x + y_intercept

def almost_equal(x, target, err = 0.01):
    return x < (target + err) and x > (target - err)

def deadzone(values, error = 0.3):
        return [0 if almost_equal(value, 0, error) else value - error for value in values]
class RotatingAverage:
    def __init__(self,size : int,start_value : float = 0):
          self.samples = [start_value]*size
          self.idx = 0
    
    def increase_index(self)->None:
         self.idx = (self.idx + 1) % len(self.samples)
    
    def set_value(self,sample : float):
        self.samples[self.idx] = sample
        self.increase_index()
    
    def get_value(self):
         return sum(self.samples)/len(self.samples)
    
    def set_through(self,value : float)->float:
         
         self.set_value(value)
         return self.get_value()