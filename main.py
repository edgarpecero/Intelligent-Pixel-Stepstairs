import machine
import utime
import time
import hcsr04
import neopixel 
import ujson
import ntptime


# Setup code:
with open('config.json', 'r') as infile:
    config = ujson.load(infile)

mode_sensors = int(config['mode_sensors'])
mode_lights = int(config['mode_lights'])
sensorOn = int(config['s_sensor_on'])
sensorAnimation = config['s_animation']

# NeoPixel Config:
PIXEL_PIN   = machine.Pin(22, machine.Pin.OUT)  # Pin connected to the NeoPixels.
PIXEL_COUNT = 238  #116 #115
np = neopixel.NeoPixel(PIXEL_PIN, PIXEL_COUNT)  
np.fill((0,0,0))                                # Start the led
np.write()                                      # strip off

# Sensor Pin config
ultrasonic_0 = hcsr04.HCSR04(echo_pin=23, trigger_pin=25)
ultrasonic_2 = hcsr04.HCSR04(echo_pin=21, trigger_pin=5)
ultrasonic_4 = hcsr04.HCSR04(echo_pin=36, trigger_pin=19)
ultrasonic_6 = hcsr04.HCSR04(echo_pin=16, trigger_pin=18)
delayStep = int(config['s_delay_step']) #After 3000 ms, they will turn off
distance_act = 69                       #sensor distance activation

# var to run a function once.
ro0 = 0
ro1 = 0
ro2 = 0
ro3 = 0

# List of ms to create delays to turnOn/turnOff without sleeping the microcontroller.
Time0 = []
Time1 = []
Time2 = []
Time3 = []

# var to save time data. 
period = 0
servertimeOn = 0

""""""" Lighting Animation """""""
# Mirror the colors to make a ramp up and ramp down with no repeated colors.
def mirror(values):
    values.extend(list(reversed(values))[1:-1])
    return values

# Linear interpolation helper:
def _lerp(x, x0, x1, y0, y1):
    return y0 + (x - x0) * ((y1 - y0)/(x1 - x0))

# Animation functions:
def off(config, np, pixel_count):
    np.fill((0,0,0))
    np.write()

def solid(config, np, pixel_count):
    solidcolors = config['colors']
    # elapsed = utime.ticks_ms() // config['period_ms']
    # current = elapsed % len(colors)
    np.fill(solidcolors[0])
    np.write()

def jump(config, np, pixel_count):
    colors = config['colors']
    elapsed = utime.ticks_ms() // config['e_period_ms']
    current = elapsed % len(colors)
    np.fill(colors[current])
    np.write()

def chase(config, np, pixel_count):
    colors = config['colors']
    elapsed = utime.ticks_ms() // config['e_period_ms']
    for i in range(pixel_count):
        current = (elapsed + i) % len(colors)
        np[i] = colors[current]
    np.write()

def smooth(config, np, pixel_count):
    # Smooth pulse of all pixels at the same color.  Interpolates inbetween colors
    # for smoother animation.
    colors = config['colors']
    period_ms = config['e_period_ms']
    ticks = utime.ticks_ms()
    step = ticks // period_ms
    offset = ticks % period_ms
    color0 = colors[step % len(colors)]
    color1 = colors[(step+1) % len(colors)]
    color = (int(_lerp(offset, 0, period_ms, color0[0], color1[0])),
             int(_lerp(offset, 0, period_ms, color0[1], color1[1])),
             int(_lerp(offset, 0, period_ms, color0[2], color1[2])))
    np.fill(color)
    np.write()

# Mirror the colors if necessary.
if config['e_mirror_colors']:
    config['colors'] = mirror(config['colors'])
# Determine the animation function to call.
animation = globals().get(config['e_animation'], off)

""""" Sensors Lighting Animation """""
def set_color(a,z,aa,zz):
    colors = config['colors']
    for i in range(a,z):
        np[i] = colors[0]
    for i in range(aa,zz):
        np[i] = colors[0] 
    np.write()
    
def blank(a,z,aa,zz):
    for i in range(a,z):
        np[i] = (0, 0, 0)
    for i in range(aa,zz):
        np[i] = (0, 0, 0) 
    np.write()


# Function to call ntptime to store the current UTC in milliseconds.
def server_time():
    try:
        # Ask to time.google.com server the current time.
        ntptime.host = "time.google.com"
        ntptime.settime()
        t = time.localtime()
        #print(t)
        # transform tuple time 't' to millisecond value.
        st = t[3]*3600 + t[4]*60 + t[5]
        return st  
    except:
        # print('no time')
        st = -1
        return st 
     
# mode_sensors = 1 - Sensors program will run.
    # Use (sensorAnimation = 0 - Default animation).
    # Different animation lighting for sensor  Coming soon...
        # servertimeOn = 1 - The program will call server_time() to ask
        # for current time, and the sensor will turn on between 17:00
        # to 6:00 México Central Time.
        # sensorOn = 1 - All sensor will be running all time.
# mode_lights = 1 - Lighting animations program will run.

while True:
    # mode_sensors = 1 - Sensors program will run.
    if mode_sensors == 1:
            # Returns an increasing millisecond counter since the Board reset.
            now = utime.ticks_ms()
            # Delay of 5000 ms to check current time.
            if now >= period + 5000:
                period += 5000.
                st = server_time()
                if  ((st > 0) and (st < 39600)) or (st > 82800):    # Turn On 17:00 Mexico Time.
                    servertimeOn = 1
                elif ((st <82800) and (st > 39600)):                # Turn Off 6:00.
                    servertimeOn = 0
                elif (st == -1):                                    # Case when Server_time() returns
                                                                    # None.
                    servertimeOn = 0
                else:
                    pass
            
            # sensorAnimation = 0 - Default animation
            # Different animation lighting for sensor will come soon...
            if sensorAnimation == 0:

                # get the distance in cm for each sensor.
                distance_0 = ultrasonic_0.distance_cm()
                distance_2 = ultrasonic_2.distance_cm()
                distance_4 = ultrasonic_4.distance_cm()
                distance_6 = ultrasonic_6.distance_cm()
                # print('Distance: ', distance_0, distance_2,distance_4,distance_6)

                """ Grouping Sensors per step """
                #sensor
                if (sensorOn == 1 or servertimeOn == 1):

                    # Compares if distance measured distance < distance_act
                    #----------- Step 0 Sensor(s)
                    if (0 < distance_0 < distance_act):
                        step_0 = 1
                    else:
                        step_0 = 0
                    #----------- Step 1 Sensor(s)
                    if (0 < distance_2 < distance_act):
                        step_1 = 1
                    else:
                        step_1 = 0
                    #----------- Step 2 Sensor(s)
                    if (0 < distance_4 < distance_act):
                        step_2 = 1
                    else:
                        step_2 = 0
                    #----------- Step 3 Sensor(s)
                    if (0 < distance_6 < distance_act):
                        step_3 = 1
                    else:
                        step_3 = 0

                    """ Steps Lighting Animation """
                    # Step 0    
                    # when someone is standing on a step, activates the turns the lights on
                    # and starts adding values of time to Time0. When the sensors stop measuring. 
                    # Compares Last Value [-1] of the list with Current time in millis (now)
                    # and turn the lights off if have elapsed delayStep value.
                    if step_0 == 1:                 # step_0 = 1 when distance_0 < distance_act
                        Time0.append(now)           # starts storing millisecond in the array
                        set_color(91,116,116,140)
                        ro0 = 1
                    elif step_0 == 0 and ro0 == 1:
                        #run function once (ro0)
                        if (now - Time0[-1]) > delayStep:
                            blank(91,116,116,140) 
                            Time0.clear()
                            ro0 = 0 
                    # Step 1
                    if step_1 == 1: 
                        Time1.append(now)
                        set_color(61,91,140,170)
                        ro1 = 1
                    elif step_1 == 0 and ro1 == 1:
                        if (now - Time1[-1]) > delayStep:
                            blank(61,91,140,170)
                            Time1.clear()
                            ro1 = 0
                    # Step 2     
                    if step_2 == 1: 
                        Time2.append(now)
                        set_color(31,61,170,200)
                        ro2 = 1
                    elif step_2 == 0 and ro2 == 1:
                        if (now - Time2[-1]) > delayStep:
                            blank(31,61,170,200)
                            Time2.clear()
                            ro2 = 0
                    # Step 3
                    if step_3 == 1:  
                        Time3.append(now)       #initialize a list of time
                        set_color(0,31,200,231)
                        ro3 = 1
                    elif step_3 ==0 and ro3 == 1:
                        if (now - Time3[-1]) > delayStep:   #3000 time in ms, compare the elapsed time since the last state,
                            blank(0,31,200,231)
                            Time3.clear()
                            ro3 = 0
                else:
                    np.fill((0,0,0))
                    np.write()

            elif sensorAnimation == 1:
                pass
                
    elif mode_lights == 1:
            animation(config, np, PIXEL_COUNT)

    else:
            np.fill((0,0,0))
            np.write()

    utime.sleep_ms(50)