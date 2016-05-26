#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

TX_PIN = 18

INTRO = [1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0]

CMD = []
CMD.append([0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1])
CMD.append([0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1])

ID = []
ID.append([1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1])
ID.append([1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0])
ID.append([0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1])
ID.append([0,1,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0,0,1,0,1,0])

DELAY = .00057
SLEEP = .016

def sendSequence(id, cmd):
    for i in INTRO+id+cmd:
        GPIO.output(TX_PIN, i)
        time.sleep(DELAY)
    GPIO.output(TX_PIN, 0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(TX_PIN, GPIO.OUT)

arg_id = int(sys.argv[1])
arg_cmd = int(sys.argv[2])

for i in range(9):
    sendSequence(ID[arg_id-1], CMD[arg_cmd])
    time.sleep(SLEEP)

GPIO.cleanup()
