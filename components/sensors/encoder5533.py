import wpilib
class BufferedEncoder5533:
    def __init__(self, encoder: 'wpilib.encoder', sample: int = 8):
        self.encoder = encoder
        self.samples = [0]*sample
        self.sampleIndex = 0
        pass
    
    def getDistance(self):
        d = self.encoder.getDistance()
        self.samples[self.sampleIndex]=d
        self.sampleIndex += 1
        self.sampleIndex = self.sampleIndex % len(self.samples)
        return (sum(self.samples)/len(self.samples))
        pass