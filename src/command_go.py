class CommandGo:
    def __init__(self, whill, measure, distance):
        print("init commnd go")
        self.whill = whill
        self.measure = measure
        self.distance = distance

    def run(self):
        if self.measure.distanceX < self.distance:
            self.whill.send_joystick(int(0), int(30))
            return True
        else: 
            print("done")
            self.whill.send_joystick(int(0), int(0))
            return False