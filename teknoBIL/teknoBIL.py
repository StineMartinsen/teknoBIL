import os
import subprocess
from tkinter import LEFT, RIGHT
from turtle import down
import Pyro4
from edurov import WebMethod
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import numpy
from lobe import ImageModel

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)

#MOTORINFO
GPIO.setup(4,GPIO.OUT) #UP
GPIO.setup(5,GPIO.OUT) #DOWN
GPIO.setup(6,GPIO.OUT) #RIGTH
GPIO.setup(26,GPIO.OUT) #LEFT

#LEDS FOR RECOGNITION
GPIO.setup(21, GPIO.OUT) #RED
GPIO.setup(20, GPIO.OUT) #GREEN
GPIO.setup(16, GPIO.OUT) #BLUE

#LEDS FOR BACKING UP AND HEADLIGHTS
GPIO.setup(23, GPIO.OUT) #BACKING LIGHTS
GPIO.setup(24, GPIO.OUT) #HEADLIGHTS

UP = False
DOWN = False
RIGHT = False
LEFT =False

camera = PiCamera()
model = ImageModel.load('/home/teknostart/teknostart2022/Lobe_test')


def control_motors():
    with Pyro4.Proxy("PYRONAME:KeyManager") as keys:
        with Pyro4.Proxy("PYRONAME:ROVSyncer") as rov:
            while rov.run:
                if keys.state('K_UP'):
                    print('Forward')
                    UP = True
                else:
                    UP = False
                if keys.state('K_DOWN'):
                    print('Down')
                    DOWN = True
                else:
                    DOWN = False
                if keys.state('K_RIGHT'):
                    print('Rigth')
                    RIGHT = True
                else:
                    RIGHT = False
                if keys.state('K_LEFT'):
                    print('Left')
                    LEFT = True
                else:
                    LEFT = False

                GPIO.output(4,UP)                
                GPIO.output(5,DOWN)
                GPIO.output(6,RIGHT)
                GPIO.output(26,LEFT)

                #DRIVINGLIGHTS
                GPIO.output(24,UP)
                GPIO.output(23,DOWN)


                ##Take picture to get input
                if keys.state('K_SPACE'):
                    take_photo()
                    # Run photo through Lobe TF model
                    result = model.predict_from_file('/home/teknostart/Pictures/image.jpg')
                    # --> Change image path
                    output(result.prediction)


# Identify prediction and turn on appropriate LED
def output(label):
    # print(label)
    if label == "ingenting":
        print("ingenting")
        sleep(5)
    if label == "mountain dew":
        print("mountain dew")
        sleep(5)
    if label == "pepsi":
        print("mountain dew")
        sleep(5)

# Take Photo
def take_photo():
    # Quickly blink status light
    print("Taking photo...")
    # Start the camera preview
    camera.start_preview(alpha=200)
    # wait 2s or more for light adjustment
    sleep(3) 
    # Optional image rotation for camera
    # --> Change or comment out as needed
    camera.rotation = 270
    #Input image file path here
    # --> Change image path as needed
    camera.capture('/home/teknostart/Pictures/image.jpg')
    #Stop camera
    camera.stop_preview()
    sleep(1)

# Create the WebMethod class
web_method = WebMethod(
    index_file=os.path.join(os.path.dirname(__file__), 'index.html'),
    runtime_functions=control_motors
)
# Start serving the web page, blocks the program after this point
web_method.serve()
