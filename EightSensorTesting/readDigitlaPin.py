from machine import Pin
from time import sleep

led = Pin(5, Pin.OUT)
button = Pin(4, Pin.IN)

while True:
  print(button.value())
  sleep(0.1)