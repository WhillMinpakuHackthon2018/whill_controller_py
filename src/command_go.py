class CommandGo:
    def __init__(self, whill, measure, distance):
        print("init commnd go")
        self.whill = whill
        self.measure = measure
        self.distance = 0

    def run(self):
        if self.distance < self.measure.distancemm:
            self.whill.send_joystick(int(30), int(0))
            return True
        else: 
            self.whill.send_joystick(int(0), int(0))
            return False