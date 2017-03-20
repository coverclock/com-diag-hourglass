#!/usr/bin/python
# Copyright 2017 Digital Aggregates Corporation, Arvada Colorado USA.
# Licensed under the terms of the GPL v2.

import time
import Adafruit_CharLCD

lcd = Adafruit_CharLCD.Adafruit_CharLCDPlate()

lcd.clear()
was = time.strftime("%a %Y-%b-%d\n %H:%M:%S %Z")
while True:
	now = time.strftime("%a %Y-%b-%d\n %H:%M:%S %Z")
	if was != now:
		lcd.message(now)
		#print now
		was = now
	time.sleep(0.2)
