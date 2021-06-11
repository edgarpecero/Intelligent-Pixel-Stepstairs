import machine
import esp32v1_hcsr04
import time
import utime



#esp32 12, 15, 27,,, #D3 D1 DD5 D6   #gpio 10, 9, 4 y 2 no jala como echo
ultrasonicPin0 = esp32v1_hcsr04.HCSR04(echo_pin=22,
                            echo_timeout_us=100000)
ultrasonicPin1 = esp32v1_hcsr04.HCSR04(echo_pin=21,
                            echo_timeout_us=100000)
ultrasonicPin2 = esp32v1_hcsr04.HCSR04(#trigger_pin=22, 
                            echo_pin=19, 
                            echo_timeout_us=100000)
# ultrasonicPin3 = esp32v1_hcsr04.HCSR04(#trigger_pin=14, 
#                             echo_pin=21, 
#                             echo_timeout_us=100000)
# ultrasonicPin4 = esp32v1_hcsr04.HCSR04(echo_pin=19,
#                             echo_timeout_us=100000)
# ultrasonicPin5 = esp32v1_hcsr04.HCSR04(#trigger_pin=22, 
#                             echo_pin=5, 
#                             echo_timeout_us=100000)
# ultrasonicPin6 = esp32v1_hcsr04.HCSR04(#trigger_pin=14, 
#                             echo_pin=17, 
#                             echo_timeout_us=100000)
# ultrasonicPin7 = esp32v1_hcsr04.HCSR04(#trigger_pin=14, 
#                             echo_pin=16, 
#                             echo_timeout_us=100000)

led2 = machine.Pin(2, machine.Pin.OUT)
led4 = machine.Pin(4, machine.Pin.OUT) 

while True:
    distance0 = ultrasonicPin0.distance_cm()
    distance1 = ultrasonicPin1.distance_cm()
    distance2 = ultrasonicPin2.distance_cm()
    # distance3 = ultrasonicPin3.distance_cm()
    # distance4 = ultrasonicPin4.distance_cm()
    # distance5 = ultrasonicPin5.distance_cm()
    # distance6 = ultrasonicPin6.distance_cm()
    # distance7 = ultrasonicPin7.distance_cm()


    
    #print(utime.ticks_add(utime.ticks_ms(), -100))
    print('Distance: ', distance0,distance1, distance2)#,distance3,distance4,distance5,distance6, distance7)
    print('///////////////////////new :')

    time.sleep_ms(350)


