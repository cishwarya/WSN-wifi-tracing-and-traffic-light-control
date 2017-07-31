import mqttSubscribeSimple
import RPi.GPIO as GPIO
import time

print("Waiting to receive location information from Special car with siren")
#Initially RED signal is ON
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)

loc=mqttSubscribeSimple.subscribe_location()
print("Location information received is as follows")
print("[Lattitude      Longitude    Type_of_car           Accuracy]")
print(loc)
#Instruct Traffic Light to switch to GREEN on receiving the Location information from Special car
GPIO.output(18,GPIO.LOW)
GPIO.setup(6,GPIO.OUT)
GPIO.output(6,GPIO.HIGH)
print "GREEN signal is ON"

#Wait for some time till the Special car with siren has crossed the signal and the change the traffic signal to RED
time.sleep(40)

GPIO.output(6,GPIO.LOW)
GPIO.output(18,GPIO.HIGH)
time.sleep(10)
print "RED signal is ON "

#System stops running
GPIO.output(18,GPIO.LOW)
