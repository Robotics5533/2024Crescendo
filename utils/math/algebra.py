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
        return [0 if almost_equal(value, 0, error) else value for value in values]