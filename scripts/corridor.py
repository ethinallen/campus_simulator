import numpy as np
from sensor import sensor
import random as rd

'''
    - at least 1 thermostat
    - at least
'''

class corridor:

    # initialize the sensor based on type and set age to 0
    def __init__(self, corridor_id):
        self.corridor_mod = None
        self.sensors = { }
        self.corridor_id = corridor_id

        num_thermostat = rd.randint(1, 3)
        num_co2 = rd.randint(3, 10)

        self.add_sensors(num_thermostat, num_co2)

    # add sensor
    def add_sensors(self, num_thermostat, num_co2):
        for i in range(num_thermostat):
            self.sensors[i] = sensor(i, 'thermostat')
        for i in range(num_co2):
            self.sensors[i + num_thermostat] = sensor(i + num_thermostat, 'c02')

if __name__ == '__main__':
    s = sensor('thermostat')
    print(np.mean(s.ttl))
