#!/usr/bin/python

import subprocess
import ephem
from datetime import datetime
import sys
import Adafruit_CharLCD as LCD
import time

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 27
lcd_d7 = 22
lcd_backlight = 4
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,lcd_columns, lcd_rows, lcd_backlight)
lcd.create_char(0, [0,0,14,27,17,31,31,31])
lcd.create_char(1, [0,4,10,10,10,17,31,14])

sun = ephem.Sun()

obs = ephem.Observer()
obs.lat = '-49.55'
obs.long= '69.83'

while 1:
    obs.date = datetime.utcnow()

    delta = min(obs.next_setting(sun).datetime(),obs.next_rising(sun).datetime()) - datetime.utcnow()

    riseset = str(delta.seconds//3600) + ":" + str(delta.seconds%3600//60).zfill(2)
    temp = subprocess.check_output("./gettemp.sh").rstrip()

    lcd.clear()
    lcd.message('\x00 ' + riseset + '\n' + '\x01 ' + temp)

    time.sleep(10)
