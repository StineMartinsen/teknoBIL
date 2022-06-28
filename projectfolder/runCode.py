from doctest import FAIL_FAST
import os
import subprocess
from tkinter import LEFT, RIGHT
from turtle import down
import Pyro4
from core import WebMethod
import RPi.GPIO as GPIO
# from lobe import ImageModel


#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.OUT) #UO
GPIO.setup(5,GPIO.OUT) #DOWN
GPIO.setup(6,GPIO.OUT) #RIGTH
GPIO.setup(26,GPIO.OUT) #LEFT

UP = False
DOWN = False
RIGHT = False
LEFT =False

INGENTING = False
KAFFEKOPP = False
VANNFLASKE = False

#MODEL FOR RECOGNITION (CHANGE FILEPATH!!)
# model = ImageModel.load('/home/teknostart/teknostart2022/Lobe_test')
def recognize(label):
    print(label)
    if label == "ingenting":
        INGENTING = True
    if label == "kaffe":
        KAFFEKOPP = True
    if label == "vann":
        VANNFLASKE = True

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
                
                #TAKE PICTURE
                if keys.state('K_SPACE'):
                    print("SPACE")
                    # --> Change image path
                    # result = model.predict_from_file('/home/teknostart/Pictures/image.jpg')
                    # output(result.prediction)

                GPIO.output(4,UP)
                GPIO.output(5,DOWN)
                GPIO.output(6,RIGHT)
                GPIO.output(26,LEFT)


# Create the WebMethod class
web_method = WebMethod(
    index_file=os.path.join(os.path.dirname(__file__), 'index.html'),
    runtime_functions=control_motors
)
# Start serving the web page, blocks the program after this point
web_method.serve()
