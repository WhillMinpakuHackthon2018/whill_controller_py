import math

class CommandTurnLeft:
    def __init__(self, whill, measure, angle_deg):
        self.whill = whill
        self.measure = measure
        self.angle_deg = angle_deg

    def run(self):
        if math.fabs(self.measure.angle_deg) < math.fabs(self.angle_deg):
            self.whill.send_joystick(int(0), int(-30))
            return True
        else: 
            print("done. turn left")
            self.whill.send_joystick(int(0), int(0))
            return False
