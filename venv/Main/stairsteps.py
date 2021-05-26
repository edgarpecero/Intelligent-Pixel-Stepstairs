#from proof import set_color
import machine, time
from machine import Pin
import neopixel, hcsr04



class STAIRSTEPS:
    """
    Setting number of pixel led by stair step
    Number of Pixel by Leght and Height
    Some neopixel sequence created
    """ 
    def __init__(self,
                red, 
                blue, 
                green, 
                speed_ms=20,
                num_leds=120,
                ledpin=5,
                ):
        """
        red: value from  0 - 255 
        blue: value from 0 - 255
        green: value from 0 - 255
        num_leds: number of leds in the strip
        ledpin: neopixel pin control 
        """ 
        self._num_leds = num_leds
        self._ledpin = neopixel.NeoPixel(machine.Pin(ledpin), num_leds)
        self._speed_ms = speed_ms
        #colors
        self._red = red
        self._blue = blue
        self._green = green 
        
    
    """Animations"""

    # All leds 1 per 1 same color
    def set_color_step_1(self, start1, mid1, end1): 
            for i in range(start1, end1):
                self._ledpin[i] = (self._red, self._blue, self._green)
                self._ledpin.write()
                time.sleep_ms(self._speed_ms)


    def set_color_step_2(self, start1, mid1, end1): 
        for i in range(start1, end1):
            self._ledpin[i] = (self._red, self._blue, self._green)
            self._ledpin.write()
            time.sleep_ms(self._speed_ms)
        
    # Clear the strip
    def clear_step_1(self, start1, end1):      
            for i in range(end1, 
                        start1-1, 
                        1):
                self._ledpin[i] = (0, 0, 0)
                self._ledpin.write()
                time.sleep_ms(self._speed_ms)
    
    #turn off everything
    def clear_all_steps(self):
            for i in range(self._num_leds):
                self._ledpin[i] = (0, 0, 0)
            self._ledpin.write()
                #time.sleep_ms(self._speed_ms)

    # Solids Colors
    def set_color_yellow(self): 
                for i in range(self._num_leds):
                    self._ledpin[i] = (255, 150, 0)
                self._ledpin.write()
                    #time.sleep_ms(self._speed_ms)
                return True

    #fade in and fade out
    def fade_in_step_1(self, start, end):
        for i in range(255, 2*256, 4):
            for j in range(start, end):
                if (i // 256) % 2 == 0:
                    val = 255 - (i & 0xff)
                else:
                    val = i & 0xff 
                self._ledpin[j] = (val, val//2, 0)
                #time.sleep_ms(1)  
            self._ledpin.write()  

    def fade_in_step_2(self, start, end):
            for i in range(255, 2*256, 4):
                for j in range(start, end):
                    if (i // 256) % 2 == 0:
                        val = 255 - (i & 0xff)
                    else:
                        val = i & 0xff 
                    self._ledpin[j] = (val, val//2, 0)
                    #time.sleep_ms(1)  
                self._ledpin.write()  
            return False 
    
        
    def fade_out_step_1(self,start, end):
        for i in range(255, 2*256, 4):
            for j in range(start, end):
                if (i // 256) % 2 == 0:
                    val = i & 0xff
                else:
                    val = 255 - (i & 0xff)
                self._ledpin[j] = (val, val//2, 0)
                #time.sleep_ms(1)
            self._ledpin.write()


    def fade_out_step_2(self,start, end):
        for i in range(255, 2*256, 4):
            for j in range(start, end):
                if (i // 256) % 2 == 0:
                    val = i & 0xff
                else:
                    val = 255 - (i & 0xff)
                self._ledpin[j] = (val, val//2, 0)
                #time.sleep_ms(1)
            self._ledpin.write()
        return False
        