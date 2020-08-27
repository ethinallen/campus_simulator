import numpy as np
import random as rd
from sensor import sensor

'''
    - at least 1 thermostat
    - at least one co2 sensor
    - random amount subject to function
'''

'''
    - contains dictionary of sensors that report a metric and a value
    - upon creation dictionary of sensor instances are created
        -
'''
class room:

    # initialize the sensor based on type and set age to 0
    def __init__(self, user_defined_room_type):
        self.room_mod   = None
        self.sensors    = { }

        num_rooms = rd.randint(10, 150)
        num_corridors = rd.randint(5, 30)

        self.add_sensors(num_rooms, num_corridors)

    # add sensor
    def add_sensors(self, num_thermostat, num_co2,):
        for i in range(num_thermostat):
            self.sensors[i] = sensor('thermostat')
        for i in range(num_thermostat):
            self.sensors[i + num_thermostat] = sensor('co2')

if __name__ == '__main__':
    s = sensor('thermostat')
    # print(s.determine_ttl('thermostat'))
