  GNU nano 2.2.6                                                      File: openvalve.py                                                                                                                  

#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("Siren.wav")
GPIO.setmode(GPIO.BCM)

print "Welcome the Portsmouth Harbour Ballast Control System.  Unauthorised access is prohibited."
print "Enter (in 100s of litres), how much water you wish to pump."
print "T42 Capacity: 24000L. T45 Capacity: 28000L.  QE2 Capacity: 85000L."

# Create list with pin numbers used in script
pinList = [2, 3, 4, 17]

# Set up GPIO on each pin number (FOR loop)
for i in pinList: GPIO.setup(i, GPIO.OUT), GPIO.output(i, GPIO.HIGH)

# Take user input and store
litres = input ("Enter litres:")

# This variable (in seconds) determines how long the solenoid valves will be open and how long water will flow.
SleepTimeL = 10

# Loop

# Change this to the pin where your solenoid is connected on your Pi GPIO board.
try:
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
