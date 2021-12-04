# Copyright The Kavinjka Software Company 2021
#
# Authour MikeC@kavinjka.com

import RPi.GPIO as GPIO
import time # for sleep functions

from signal import signal, SIGINT # for Cntrl-C
from sys import exit

# Initialize the  GPIO Infrastructure to BCM (Broadcom SOC channel)
GPIO.setmode(GPIO.BCM)

# Define the Green LED GPIO port as an output
GREEN = 26
GPIO.setup(GREEN, GPIO.OUT)

# Define an exit handler for the program (called on Cntrl-C)
def ctrl_c_handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    GPIO.cleanup()
    exit(0)

# setup the Ctrl-C handler
signal(SIGINT, ctrl_c_handler)

# infinite loop for the main thread (Use Cntrl-C to exit)
while True:
  # Turn the Green LED On
  GPIO.output(GREEN, GPIO.HIGH)

  # Sleep for 2 Seconds
  time.sleep(2)

  # Turn off the Green LED
  GPIO.output(GREEN, GPIO.LOW)

  # Sleep for 2 Seconds
  time.sleep(2)
