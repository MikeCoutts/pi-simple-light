# pi-simple-light
A Simple Raspberry PI Python program to show the use of a GPIO Output pin to control a single LED. 

Simple infinite loop causing an LED to "Flash" on GPIO Pin 26

![Alt text](https://github.com/MikeCoutts/pi-simple-switch/blob/main/images/IMG_20211103_225959778.jpg?raw=true "Traffic Lights")

# Simple Raspberry Pi Bread Board wiring for this project
[Buzzer](https://www.amazon.com/dp/B07S85WRSZ?psc=1&ref=ppx_yo2_dt_b_product_details) ground on 5V GND line with +ve into GPIO 23.

[Multi Color LED] Blue (GPIO 17), Green (GPIO 23) and Red (GPIO 22) connected to BGR Anodes via 10K Ohm Resitors with Cathode to Ground.

[Individual LED's] Red (GPIO 13), Amber/Yellow (GPIO 19), Green (GPIO 26) connected to Red/Amber/Green Anodes via 10K Ohm resitors.

10K Ohm resiter supplying power to momentary switch with a Blue line (connected to GPIO Input 16) being drawn down by the Blue LED.

# Operation of the Program
import RPi.GPIO, time, signal.signal, signal.SIGINT and sys.exit

Define the Green LED Output as GPIO Pin 26

Define the exit handler as we will be using an infinite loop

Enter an infinite loop (while True:)
  Turn on Green LED, Sleep for 2 seconds
  Turn off Green LED, Sleep for 2 seconds
