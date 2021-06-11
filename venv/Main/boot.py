try:
  import usocket as socket
except:
  import socket
from machine import Pin
from time import time
import network

import esp
esp.osdebug(None)
import gc
gc.collect()

#ssid = 'INFINITUM7bsj'
ssid = 'INFINITUM259F_2.4'

#password = 'd061436793'
password = 's3My8K5sG2'



station = network.WLAN(network.STA_IF)
wstime = time
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

led32 = Pin(32, Pin.OUT)
led33 = Pin(33, Pin.OUT)
