class CommandForward:
    def __init__(self, whill, measure, distance):
        self.whill = whill
        self.measure = measure
        self.distance = distance

    def run(self):
        if self.measure.distanceX < self.distance:
            self.whill.send_joystick(int(30), int(0))
            return True
        else: 
            print("done. forward")
            self.whill.send_joystick(int(0), int(0))
            return False