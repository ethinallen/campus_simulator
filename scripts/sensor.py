import numpy as np
import random as rd

'''
    - Need to give them different reporting frequencies
'''

class sensor:

    # initialize the sensor based on type and set age to 0
    def __init__(self, user_defined_sensor_type,):
        self.type = user_defined_sensor_type
        self.info = None
        self.age = 0
        self.meter_id = None
        self.ttl = self.determine_ttl()

    def getOlder(self):
        self.age += 1
        print('I aged :) {}'.format(self.age))

    # determine the life of the sensor (hours)
    def determine_ttl(self, ):
        s = np.random.poisson(17532, 1)
        return s

if __name__ == '__main__':
    s = sensor('thermostat')
    print(np.mean(s.ttl))
    # print(s.determine_ttl('thermostat'))
