from MotorDriver import MotorDriver  
from LiDAR_Sensor import LiDAR
import serial, time 
#import Jetson.GPIO as GPIO

# Setup motors
#GPIO.setmode(GPIO.BOARD)
rover_motor_control = MotorDriver(11, 15, 32, 33)

# Setup LiDAR UART
lidar_sensor = LiDAR('COM4', 115200)

try:
    while True:
        dist = lidar_sensor.read_lidar_distance()
        if dist:
            print(f"Distance: {dist} cm")
            if dist < 30:  # obstacle within 30 cm
                print("Obstacle detected! Backing up and turning...")
                rover_motor_control.stop()
                rover_motor_control.move_backwards()
                #time.sleep(1)
                rover_motor_control.stop()
                rover_motor_control.turn_right()
                #time.sleep(1)
            else:
                print("Path clear → moving forward")
                rover_motor_control.move_forwards()
                #time.sleep(1)

except KeyboardInterrupt:
    rover_motor_control.stop()
    #GPIO.cleanup()
    lidar_sensor.close_lidar()
