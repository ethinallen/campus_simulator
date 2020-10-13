import numpy as np
import random as rd
from sensor import sensor

'''
    - at least 1 thermostat
    - at least one co2 sensor
    - random amount subject to function
    - need to pass in the building and room id to make composite sensor id
'''

'''
    - contains dictionary of sensors that report a metric and a value
    - upon creation dictionary of sensor instances are created
'''
class room:

    # initialize the sensor based on type and set age to 0
    def __init__(self, room_id, numRows):
        self.room_mod   = None
        self.sensors    = { }
        self.id = room_id

        num_thermostat = rd.randint(1, 3)
        num_co2 = rd.randint(3, 10)

        self.add_sensors(num_thermostat, num_co2, numRows)

    # add sensor
    def add_sensors(self, num_thermostat, num_co2, numRows):
        for i in range(num_thermostat):
            self.sensors[i] = sensor(i, 'thermostat', numRows)
        for i in range(num_co2):
            self.sensors[i + num_thermostat] = sensor(i + num_thermostat, 'c02', numRows)

if __name__ == '__main__':
    s = sensor('thermostat')
