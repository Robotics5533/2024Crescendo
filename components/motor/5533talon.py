from phoneix6 import hardware, configs, signals, controls

class Talon5533:
    def __init__(self, id):
        self.talonmotor = hardware.TalonFX(id)
        self.controller = controls.DutyCycle(0)
    def set(self, value):
        self.controller.output = value
        self.talonmotor.set_controller(self.controller)