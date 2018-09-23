class CommandStop:
    def __init__(self, whill, measure, msec):
        self.whill = whill
        self.measure = measure
        self.msec = msec
        self.__count = 0

    def run(self):
        self.whill.send_joystick(int(0), int(0))
        if self.__count * self.measure.interval_msec <= self.msec:
            self.__count += 1
            return True
        else: 
            print("done. stop")
            return False

