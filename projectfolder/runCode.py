from doctest import FAIL_FAST
import os
from pickle import FALSE
import subprocess
from tkinter import LEFT, RIGHT
from turtle import down
import Pyro4
from core import WebMethod
import RPi.GPIO as GPIO



#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.OUT) #UP
GPIO.setup(5,GPIO.OUT) #DOWN
GPIO.setup(6,GPIO.OUT) #LEFT
GPIO.setup(26,GPIO.OUT) #RIGHT

UP = False
DOWN = False
RIGHT = False
LEFT =False

INGENTING = False
KAFFEKOPP = False
VANNFLASKE = False



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
                # if keys.state('K_SPACE'):
                    # print("SPACE")
                # if COMPARE == True:
                #     # result = compare()
                #     # recognize(result)
                #     print("PENIS")
                #     COMPARE = False
                    
                    

                GPIO.output(4,UP)
                GPIO.output(5,DOWN)
                GPIO.output(6,LEFT)
                GPIO.output(26,RIGHT)


# Create the WebMethod class
web_method = WebMethod(
    index_file=os.path.join(os.path.dirname(__file__), 'index.html'),
    runtime_functions=control_motors
)
# Start serving the web page, blocks the program after this point
web_method.serve()
