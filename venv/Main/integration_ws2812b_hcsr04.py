import machine, hcsr04
import time, utime
import stairsteps, neopixel


"""Settings"""
#Led Config
PixelControl = stairsteps.STAIRSTEPS(red=255,green=150,blue=0) #Yellow
Delay = 1500 #After 3000 ms, they will turn off

#Sensor Pin config
distance_act = 50 #sensor distance activation
ultrasonicPin1 = hcsr04.HCSR04(trigger_pin=13, echo_pin=12)
ultrasonicPin2 = hcsr04.HCSR04(trigger_pin=22, echo_pin=15)

#run a function once
ro1 = 0 
ro2 = 0                     

#List of ms to create delays to turnOn/turnOff without sleeping the microcontroller
Time1 = []
Time2 = []


"""Stais Steps Settings"""
# Stair Step 1; parameters for lenght (first_pixel, last_pixel)
def step_1_on():
    PixelControl.fade_in_step_1(22,32)
def step_1_off():
    PixelControl.fade_out_step_1(22,32)
# Stair Step 2; parameters for lenght (first_pixel, last_pixel)
def step_2_on():
    PixelControl.fade_in_step_2(10,19)
def step_2_off():
    PixelControl.fade_out_step_2(10,19)
 


while True:
    now = utime.ticks_ms() #time in ms
    distance_1 = ultrasonicPin1.distance_cm() 
    distance_2 = ultrasonicPin2.distance_cm()
        
    print('Distance1:', distance_1, 'cm')
    print('Distance2:', distance_2, 'cm')
    print('now', now)

    #      Stair Step 1
    if ((distance_1) <= distance_act) and ((distance_1) > -1):  #Turn the lights on when the sensors detects a distance
                                                                #less than distance_activation (50 cm)
        Time1.append(now)       #initialize a list of time
        if (ro1 == 0):          #runs Step_1_on() function once   
            step_1_on()
            ro1 = 1
    if (ro1 == 1) and (distance_1 > distance_act):
            if (now - Time1[-1]) > Delay:   #3000 time in ms, compare the elapsed time since the last state, 
                                            #if gratear than Delay(3000ms), then lights turn off after 3 segs.
                step_1_off()
                ro1 = 0
            else:
                pass
    if (ro1 == 0) and (distance_1 > distance_act):  #Nothing happends, sensor is reading
        ro1 = 0
        Time1.clear() #empty list

    #      Stair Step 2
    if ((distance_2) <= distance_act) and ((distance_2) > -1):
        Time2.append(now)
        if (ro2 == 0):
            step_2_on()
            ro2 = 1
    if (ro2 == 1) and (distance_2 > distance_act):
            if (now - Time2[-1]) > Delay: #3000 time in ms
                step_2_off()
                ro2 = 0
            else: 
                pass
    if (ro2 == 0) and (distance_2 > distance_act):
        ro2 = 0
        Time2.clear()

    #       Stair Step 3
    """"""""""""""
    time.sleep_ms(10)