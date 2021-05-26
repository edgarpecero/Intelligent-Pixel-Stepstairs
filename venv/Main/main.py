import machine, hcsr04
import time, utime, ntptime
import stairsteps, neopixel

"""Settings"""
#Led Config
PixelControl = stairsteps.STAIRSTEPS(red=255,green=150,blue=0, num_leds=20) #Yellow
Delay = 1500 #After 3000 ms, they will turn off

#Sensor config
distance_act = 50 #sensor activations
ultrasonicPin1 = hcsr04.HCSR04(trigger_pin=13, echo_pin=12)
ultrasonicPin2 = hcsr04.HCSR04(trigger_pin=22, echo_pin=15)

#run a function once
ro1 = 0 
ro2 = 0                     

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

# Entire Stairs Step Yellow; parameters for lenght (first_pixel, last_pixel)
def step_1_yellow_on():
    PixelControl.set_color_yellow()
def step_1_all_off():
    PixelControl.clear_all_steps()


def web_page(): 

  if led33.value() == 1:
    gpio_state= ''
  else:
    gpio_state= 'checked'
  html = """
  <html>
    <head>
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <meta http-equiv="refresh" content="600">
          <a href="https://icons8.com/icon/XBJfETMfZHpS/light"></a>
        <style>
            body{font-family:Arial;                 text-align: center;                 margin: 0px auto;                 padding-top:30px;              }
            h2 { font-size: 2.0rem; }
            .switch{position:relative;display:inline-block;width:120px;height:68px}
            .switch input{display:none}
            .slider{position:absolute;top:0;left:0;right:0;bottom:0;background-color:#ccc;border-radius:34px}
            .slider:before{position:absolute;content:"";height:52px;width:52px;left:8px;bottom:8px;background-color:#fff;-webkit-transition:.4s;transition:.4s;border-radius:68px}
            input:checked+.slider{background-color:#2196F3}
            p { font-size: 3.0rem; }
            input:checked+.slider:before{-webkit-transform:translateX(52px);-ms-transform:translateX(52px);transform:translateX(52px)}
        </style>
        
        <script> 
          function toggleCheckbox(element) { var xhr = new XMLHttpRequest(); 
          if(element.checked){ xhr.open("GET", "/?led=on", true); }
          else { xhr.open("GET", "/?led=off", true); } xhr.send(); }
        </script>
    </head>
    <body>
        <h2>Lumina Web Server</h2>
        <p><img src="https://img.icons8.com/nolan/96/light.png"/>
        </p>
        </p>
          <label class="switch"> 
          <input type="checkbox" onchange="toggleCheckbox(this)" %s>
          <span class="slider">
          </span>
          </label>
        </p>
    </body>
  </html>""" % (gpio_state)
  
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def server_time():
     ntptime.host = "time.google.com"
     ntptime.settime()
     t = time.localtime()
     current_time = t[3]*3600 + t[4]*60 + t[5]
     return current_time      

while True:
  #socket accept()
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  #socket receive()
  request = conn.recv(1024)
  #socket send()
  request = str(request)
  print('Content = %s' % request)
  
  # Main Loop // Activation after 6 pm
  st = server_time()
  

  print(st)
  if  ((st > 0) and (st < 39600)) or (st > 82800): #turnOn_time: 6 pm
    led32.value(1)
    pass
  elif ((st <82800) and (st > 39600)):#turnOff_time: 6 am
    #step_1_all_off()
    led32.value(0)

  

  #Receive info from client
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  
  if led_on == 6:
    #step_1_yellow_on()    
    led33.value(1)    
  if led_off == 6:
    step_1_all_off()
    led33.value(0)
  

  




  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()