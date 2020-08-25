import numpy as np

class sensor:

    # initialize the sensor based on type and set age to 0
    def __init__(self, user_defined_sensor_type):
        type = user_defined_sensor_type
        age = 0
        self.ttl = self.determine_ttl()

    def getOlder(self):
        self.age += 1

    # determine the life of the sensor
    def determine_ttl(self):
        s = np.random.poisson(1, 10000)
        return s


if __name__ == '__main__':
    s = sensor('termostat')
    print(np.mean(s.ttl))
    # print(s.determine_ttl('thermostat'))
