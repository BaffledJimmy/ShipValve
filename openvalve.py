#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("Siren.wav")

GPIO.setmode(GPIO.BCM)

print "Welcome the RN Ballast Control System.  Unauthorised access is prohibited."

# Create list with pin numbers used in script

pinList = [2, 3, 4, 17]

for i in pinList: GPIO.setup(i, GPIO.OUT) GPIO.output(i, GPIO.HIGH)

# This variable (in seconds) determines how long the solenoid valves will be open and how long water will flow.

SleepTimeL = 10

# Loop

try:
# Change this to the pin where your solenoid is connected on your Pi GPIO

GPIO.output(17, GPIO.LOW) 
time.sleep(SleepTimeL);
GPIO.cleanup()
print "Ship Ballast Valve Opened!"
pygame.mixer.Sound("Siren.mp3")

# End program cleanly with keyboard
except KeyboardInterrupt:
print " Exitting"

# Reset GPIO settings
GPIO.cleanup()
