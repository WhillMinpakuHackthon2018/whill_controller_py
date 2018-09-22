class CommandGo:
    def __init__(self, whill, measure, distance):
        print("init commnd go")
        self.whill = whill
        self.measure = measure
        self.distance = 0

    def run(self):
        if  self.measure.distancemm <= self.distance:
            self.whill.send_joystick(int(30), int(0))
            return True
        else: 
            print("done")
            self.whill.send_joystick(int(0), int(0))
            return False