#import Jetson.GPIO as GPIO
import time

class MotorDriver:
    def __init__(self, in1=11, in2=15, in3=32, in4=33):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4

        #GPIO.setup(in1, GPIO.OUT,initial=GPIO.LOW)
        #GPIO.setup(in2, GPIO.OUT,initial=GPIO.LOW)
        #GPIO.setup(in3, GPIO.OUT,initial=GPIO.LOW)
        #GPIO.setup(in4, GPIO.OUT,initial=GPIO.LOW)

    def move_forwards(self):
        #GPIO.output(self.in1,GPIO.HIGH)
        #GPIO.output(self.in2,GPIO.LOW)
        #GPIO.output(self.in3,GPIO.HIGH)
        #GPIO.output(self.in4,GPIO.LOW)
        print("Moving forward")
    def turn_right(self):
        #GPIO.output(self.in1,GPIO.HIGH)
        #GPIO.output(self.in2,GPIO.LOW)
        #GPIO.output(self.in3,GPIO.HIGH)
        #GPIO.output(self.in4,GPIO.HIGH)
        print("Turning Right")
    def turn_left(self):
        #GPIO.output(self.in1,GPIO.HIGH)
        #GPIO.output(self.in2,GPIO.HIGH)
        #GPIO.output(self.in3,GPIO.HIGH)
        #GPIO.output(self.in4,GPIO.LOW)
        print("Turning left")
    def move_backwards(self):
        #GPIO.output(self.in1,GPIO.LOW)
        #GPIO.output(self.in2,GPIO.HIGH)
        #GPIO.output(self.in3,GPIO.LOW)
        #GPIO.output(self.in4,GPIO.HIGH)
        print("Moving backwords")
    def stop(self):
        #GPIO.output(self.in1,GPIO.HIGH)
        #GPIO.output(self.in2,GPIO.HIGH)
        #GPIO.output(self.in3,GPIO.HIGH)
        #GPIO.output(self.in4,GPIO.HIGH)
        print("Stopping")
