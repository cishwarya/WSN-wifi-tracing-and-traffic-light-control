# WSN-wifi-tracing-and-traffic-light-control
﻿﻿A Car-to-X Communication Framework for autonomous cars with Wi-Fi Car Tracing and Traffic Light Control Optimizing
  ===================================================================================================================
  
  This project demonstrates a Car-to-X communication framework for autonomous cars, in which car Wi-Fi localization, infrastructure control, 
and wireless communication between car and infrastructure is implemented.

  This framework is built considering three use cases. First scenario is communication between normal car and traffic light. 
Second is communication between special car (without siren) and traffic light. 
The third scenario is communication between special car (with siren) and traffic light. The difference between second and third scenario is
that tradional server based communication is used in second whereas MQTT based communication is used in thrid scenario.
In third scenario. Traffic Light is the subscriber and Special car is the publisher which publishes the data.
The communication between the publisher and the subscriber nodes happen via MQTT message broker which is implemented in the special car RPi.

Python is used for the framework development.  Raspberry PI (RPi) is used to test the demo.
Raspbian operating system (OS) for RPi is downloaded on the SD card and installed. 
A Linux server virtual machine (VM) with Ubuntu OS running is built. 
Other installation required to run the project are as follows:

1. pip
2. selenium
3. uuid
4. paho MQTT
5. mosquito message broker

SERVER BASED COMMUNICATION:
-----------------------------
 For the server based communication, the files “normal_car.py”, “special_car.py”is loaded in one RPi and 
“TrafficLight.py” is loaded in another RPi and executed. 
The “server.py” should be executed on Linux server VM.

MQTT BASED COMMUNICATION:
-----------------------------
  For MQTT based communication, the files “special_car_siren.py”, and“mqttPublishMultiple.py” are loaded in the special car RPi and executed. 
In another RPi which denotes Traffic light, “mqttSubscribeSimple.py” and “TrafficLight_mqtt.py” are loaded and executed. 

EXECUTION OF SCENARIO 1: NORMAL car:
=======================================
1. First, TrafficLight.py  is executed on a Raspberry Pi. In TrafficLight.py a socket is used to receive a UDP packet at 8080 port. 
The packet contains the instruction to control the traffic light.
2. server.py code is executed on Linux system.In server, a socket is used to receive UDP packet from port 2333. 
Since the car type is normal in this scenario, when the server code is executed, first it runs an algorithm to decide the nearest traffic light for the car.
Next the server runs an algorithm to generate an optimized traffic light signal.
After the new traffic instruction is generated, server sends a UDP packet containing traffic light instruction to the nearest traffic light.
3. normal_car.py code is executed on another Raspberry pi.
In normal_car.py, a socket is used to send location information as a UDP packet and to collect the optimized traffic instruction.

EXECUTION OF SCENARIO 2: Special car without siren:
=====================================================
Step 1 and 2 is same as scenario 1. Instead of normal_car.py, special_car.py code is executed. Since the car type is 'special',
this car make the traffic light to TURN GREEN for it. 

EXECUTION OF SCENARIO 3: Special car with siren (MQTT based communication):
===========================================================================
1. First trafficLight_mqtt.py code is executed on a RPi. Traffic Light is the subscriber which subscribes on the topic “/location” to the broker.
2. LED is connected to RPi GPIO.
3. “special_car_siren.py” code is executed on another RPi. This acts as the publisher which publishes its location data retrieved from 
Google Geolocation API to the message broker with the message topic “/location”.
4. Once the location data is published from the special car, the Traffic Light signal state changes to GREEN 
and the location information is received by the Traffic Light. 
After few seconds, the traffic light changes to RED state, assuming that the special car has crossed the traffic junction 
and the program stops execution.



