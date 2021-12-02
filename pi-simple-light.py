# Copyright The Kavinjka Software Company 2021
#
# Authour MikeC@kavinjka.com

import RPi.GPIO as GPIO
import time # for sleep functions

from signal import signal, SIGINT # for Cntrl-C
from sys import exit

# define the GPIO ports for the Green LED
green = 26

# Define an exit handler for the program (called on Cntrl-C)
def CntrlCHandler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    GPIO.cleanup()
    exit(0)

# setup  the Cntrl-C handler
signal(SIGINT, CntrlCHandler)

# Initialize the  GPIO Infrastructure to BCM (Broadcom SOC channel)
GPIO.setmode(GPIO.BCM)

# Setup the Green GPIO Output Pin
GPIO.setup(green, GPIO.OUT) 

# infinate loop for the main thread (Use Cntrl-C to exit)
while True:
  # Turn the Green LED On
  GPIO.output(green, GPIO.HIGH)

  # Sleep for 2 Seconds
  time.sleep(2)

  # Turn off the Green LED
  GPIO.output(green, GPIO.LOW)

  # Sleep for 2 Seconds
  time.sleep(2)
