import numpy as np
import random as rd

'''
    - Need to give them different reporting frequencies
'''

class sensor:

    # initialize the sensor based on type and set age to 0
    def __init__(self, sensor_id, user_defined_sensor_type):
        self.type = user_defined_sensor_type
        self.age = 0
        self.replacement_wait = 0
        self.deaths = 0
        self.meter_id = sensor_id
        self.ttl = self.determine_ttl(self.type)

    # iterate the age of the sensor
    def getOlder(self):
        if self.age < self.ttl and self.replacement_wait == 0:
            self.age += 1

        elif self.replacement_wait > 0:
            self.replacement_wait -= 1
        else:
            self.ttl = self.determine_ttl(self.type)
            self.deaths += 1
            self.replace_sensor()
            pass

    # average sensor replacement poisson distributed at 72 hours
    def replace_sensor(self):
        self.replacement_wait = np.random.poisson(72, 1)[0]
        self.age = 0
        # print('SENSOR REPLACED AFTER {} HOURS'.format(self.replacement_wait))

    # generate a sensor value subject to type
    def generateValue(self):
        return None

    # determine the life of the sensor (hours)
    def determine_ttl(self, sensor_type):
        s = np.random.poisson(17532, 1)[0]
        return s

if __name__ == '__main__':
    s = sensor('thermostat')
    print(np.mean(s.ttl))
