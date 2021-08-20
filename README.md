# Smart Pixel Stairsteps
Automation project - Intelligent Pixel Step Stairs code in micropython. 
This is an automation project, using ESP32 to connect to WiFi and 4 HSR04 sensor to get a presence signal and turn on the Step Leds.
Also, the whole project is controlled using a Single Page Application - API

The comunication between MCU and Web App, it will use the web REPL as an 'API' to send a Original configuration to the board and save it as a config.json file.

This is the Web Application Interface. The two green buttons select the 2 main configuration for the systems
  - Sensors
  - Effects
Then, new config options will be displayed.

Sensors' Mode:
  In the default config for Sensor Mode, the system will be active between 7 p. m. and 7 a. m. (UTC-6 - using ntpserver to get datetime), lights' color will be white and   a delay of 2 seconds. 
  During the active time, lights will be turn on while something or someone stands on the steps.
  
  Other functions:
    - Color Selection
    - Delay for turn off the lights.
    
Effects' Mode:
  In the default config for Effect Mode, the system will remenber the last color selected. You can choose among colors, you can choose differents types of animation.
  
  Other functions:
    - Speed (milliseconds)
    - Mirroring colors

![efectos](https://user-images.githubusercontent.com/81655331/130261845-1ab0d5a7-99b7-46d9-95fe-bb26f4312e74.png)

![sensores](https://user-images.githubusercontent.com/81655331/130261869-52404923-8b82-457e-bad5-77ad918222cf.png)

