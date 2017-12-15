# GNU nano 2.2.6                                                      File: openvalve.py

#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("Siren.wav")
GPIO.setmode(GPIO.BCM)

print ("Welcome the Portsmouth Harbour Ballast Control System.  Unauthorised access is prohibited.")
print ("Enter (in 100s of litres), how much water you wish to pump.")
print ("T42 Capacity: 24000L. T45 Capacity: 28000L.  QE2 Capacity: 85000L.")

# Create list with pin numbers used in script
pinList = [2]

# Set up GPIO on each pin number (FOR loop)
for i in pinList:
    GPIO.setup(i, GPIO.OUT), GPIO.output(i, GPIO.LOW)

# Take user input and store
SleepTimeL = 10
while(1):
    litres = input("Enter litres:")

    # This variable (in seconds) determines how long the solenoid valves will be open and how long water will flow.

    # Loop

    # Change this to the pin where your solenoid is connected on your Pi GPIO board.

    # solenoid valve capacity is 3.5 litres/min
    # 1 litre in 30.00 seconds
    try:
        if((litres % 100) == 0):

            SleepTimeL = (litres * 30.0)
            GPIO.output(2, GPIO.HIGH)
            time.sleep(SleepTimeL)
            GPIO.output(2, GPIO.LOW)
            GPIO.cleanup()
            print ("Ship Ballast Valve Opened!")
            pygame.mixer.play()
        else:
            print("Enter in 100s of litres.")

    # End program cleanly with keyboard
    except KeyboardInterrupt:
        print (" Exitting")

    # Reset GPIO settings
    GPIO.cleanup()
