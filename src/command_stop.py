class CommandStop:
    def __init__(self, whill, measure, count):
        self.whill = whill
        self.measure = measure
        self.count = count
        self.__count = 0

    def run(self):
        self.whill.send_joystick(int(0), int(0))
            
        if self.__count =< self.count:
            return True
        else: 
            print("done. stop")
            return False

        self.__count += 1
