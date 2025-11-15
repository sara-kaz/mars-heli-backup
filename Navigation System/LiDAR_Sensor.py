import serial, time

class LiDAR:
    def __init__(self, port, baud):
        self.port = port
        self.baud = baud
        self.ser = serial.Serial(port, baud)

    def read_lidar_distance(self):
        if self.ser.read() == b'\x59':
            if self.ser.read() == b'\x59':  # Second header byte
                data = self.ser.read(7)
                distance = data[0] + data[1]*256
                strength = data[2] + data[3]*256
                print(f"Distance: {distance} cm, Strength: {strength}")
                return distance
    
    def close_lidar(self):
        self.ser.close()
