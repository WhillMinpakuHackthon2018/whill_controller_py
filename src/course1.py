#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# コース１のスクリプト

import time
from whill import ComWHILL
from command_forward import CommandForward
from command_turn_left import CommandTurnLeft
from command_turn_right import CommandTurnRight
from command_stop import CommandStop
from command_http import CommandHttp
from measure import Measure

whill = ComWHILL(port='/dev/tty.usbserial-FT2K21HW')
request_speed_mode = 0
measure = Measure()

commands = [
    CommandForward(whill, measure, 1.2),    
    CommandTurnRight(whill, measure, 45.0),
    CommandHttp("http://192.168.21.214:3000/change1"),
    CommandStop(whill, measure, 5000),
    CommandTurnLeft(whill, measure, 90.0),
    CommandForward(whill, measure, 1.0), 
    CommandTurnRight(whill, measure, 45.0),
    CommandHttp("http://192.168.21.214:3000/change2"),
    CommandStop(whill, measure, 5000),
    CommandTurnLeft(whill, measure, 135.0),
    CommandForward(whill, measure, 1.0), 
    CommandTurnRight(whill, measure, 45.0),
    CommandHttp("http://192.168.21.214:3000/change3"),
    CommandStop(whill, measure, 5000),
    CommandTurnLeft(whill, measure, 135),
    CommandForward(whill, measure, 1.2),
    CommandHttp("http://192.168.21.214:3000/change4"),
]

def callback1():
    global whill, measure
    measure.update(whill)

def main():
    whill.register_callback('data_set_1', callback1)
    print("register_callback")
    whill.start_data_stream(int(measure.interval_msec), 1, request_speed_mode)
    print("start_data_stream")

    current = 0

    while True:
        time.sleep(measure.interval_msec / 1000.0)
        whill.refresh()

        if commands[current].run() == False:
            current += 1
            if len(commands) == current:
                break
            print("next")
            measure.reset()

    print("end")

if __name__ == "__main__":
    main()