import numpy as np
import random as rd
import requests
import uuid

'''
    - Need to give them different reporting frequencies
'''

class sensor:

    # initialize the sensor based on type and set age to 0
    def __init__(self, user_defined_sensor_type, numRows, *attrs):
        self.entropy = np.random.normal(70, 5, numRows)

        if attrs:
            attrs=attrs[0]
            self.type = 'thermostat'
            self.replacement_wait = attrs['info']['replacement_wait']
            self.id = attrs['id']
            self.age = attrs['info']['age']
            self.ttl = attrs['info']['latest_ttl']

        else:
            self.type = user_defined_sensor_type
            self.age = 0
            self.replacement_wait = 0
            self.deaths = 0
            self.id = np.int64(str(uuid.uuid4().int)[:7])
            self.ttl = int(self.determine_ttl(self.type))


    # iterate the age of the sensor
    def getOlder(self, index):
        if self.age < self.ttl and self.replacement_wait == 0:
            self.age += 1
            deviation = self.entropy[index]
            deviation = np.int64(deviation)
            return deviation

        elif self.replacement_wait > 0:
            self.replacement_wait -= 1
            return -999

        else:
            self.ttl = self.determine_ttl(self.type)
            self.deaths += 1
            self.replace_sensor()
            return -999


    # average sensor replacement poisson distributed at 72 hours
    def replace_sensor(self):
        self.replacement_wait = int(np.random.poisson(72, 1)[0])
        self.age = 0

    # generate a sensor value subject to type
    def generateValue(self):
        return None

    # determine the life of the sensor (hours)
    def determine_ttl(self, sensor_type):
        s = np.random.poisson(17532, 1)[0]
        return np.int(s)

    #
    def reportData(self, ):
        return None

if __name__ == '__main__':
    s = sensor('thermostat')
    print(np.mean(s.ttl))
