#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, SpeedPercent, MoveTank,MediumMotor,OUTPUT_A, OUTPUT_B,OUTPUT_C,OUTPUT_D
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import TouchSensor,ColorSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
import time,os
os.system('setfont ' + 'Lat15-Terminus24x12')


sound=Sound()
sound.speak('hello')
