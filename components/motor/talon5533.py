from phoenix6 import hardware, controls

class Talon5533:
    def __init__(self, id: int):
        self.talonmotor = hardware.TalonFX(id)
        self.controller = controls.DutyCycle(0)

    def set(self, value):
        self.controller.output = value
        self.talonmotor.set_controller(self.controller)