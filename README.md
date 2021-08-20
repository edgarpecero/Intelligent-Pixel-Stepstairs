# Smart Pixel Stairsteps
Automation project - Intelligent Pixel Step Stairs code in micropython. 
This is an automation project, using ESP32 to connect to WiFi and 4 HSR04 sensor to get a presence signal and turn on the Step Leds.
Also, the whole project is controlled using a Single Page Application - API

The comunication between MCU and Web App, it will use the web REPL as an 'API' to send a Original configuration to the board and save it as a config.json file.

This is the Web Application Interface. The two green buttons select the 2 main configuration for the systems
  - Sensors
  - Effects

Then, new config options will be displayed.

- Sensors' Mode:
    In the default config for Sensor Mode, the system will be active between 7 p. m. and 7 a. m. (UTC-6 - using ntpserver to get datetime), lights' color will be white    and   a delay of 2 seconds. 
    During the active time, lights will be turn on while something or someone stands on the steps.

    Other functions:
    
      - Color Selection
     
      - Delay for turn off the lights
    
- Effects' Mode:
    In the default config for Effect Mode, the system will remenber the last color selected. You can choose among colors, you can choose differents types of animation.

    Other functions:
    
      - Speed (milliseconds)
      
      - Mirror colors

![efectos](https://user-images.githubusercontent.com/81655331/130261845-1ab0d5a7-99b7-46d9-95fe-bb26f4312e74.png)

![sensores](https://user-images.githubusercontent.com/81655331/130261869-52404923-8b82-457e-bad5-77ad918222cf.png)

Sensor Mode
Lights will turn on when something or someone stands on the steps. The sensor HCSR04 will trigger the signal, which is read by the MCU and turn on the lights with the config load from the Web App.

![merge](https://user-images.githubusercontent.com/81655331/130284177-35e7d380-8596-4516-b313-64558709a7bc.png)


Effects Mode
You can choose among differents animations:
  
    - Chase

    - Jump

    - Smooth

    - Solid

    - Turn Off
    
And combine animations with your prefered color.

![4](https://user-images.githubusercontent.com/81655331/130281744-0e61e070-c176-4d90-96b1-e5638dc148e7.jpg)
![5](https://user-images.githubusercontent.com/81655331/130281745-5605a936-736b-4d28-8b89-bb1efa696e00.jpg)
