
#!/usr/bin/env python3

# whill module example package
# Copyright (c) 2018 WHILL, Inc.
# This software is released under the MIT License.


import time
from whill import ComWHILL

whill = ComWHILL(port='/dev/tty.usbserial-FT1HNPEN')
while True:
    whill.send_joystick(int(10), int(0))
    time.sleep(0.05)
