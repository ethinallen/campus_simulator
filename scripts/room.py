import numpy as np
import random as rd
from sensor import sensor
import uuid

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
    def __init__(self, room_id, numRows, *attrs):
        self.room_mod   = None
        self.sensors    = { }

        if attrs:
            attrs=attrs[0]
            for i, sensorID in enumerate(attrs['info']):
                sensor_attributes = {'id': sensorID, 'info' : attrs['info'][sensorID]}
                self.sensors[i] = sensor('thermostat', numRows, sensor_attributes)
                self.id = attrs['id']
        else:
            self.id = np.int64(str(uuid.uuid4().int)[:7])

            num_thermostat = rd.randint(1, 2)
            num_co2 = rd.randint(1, 3)

            self.add_sensors(num_thermostat, num_co2, numRows)

    # add sensor
    def add_sensors(self, num_thermostat, num_co2, numRows):
        for i in range(num_thermostat):
            self.sensors[i] = sensor('thermostat', numRows)
        for i in range(num_co2):
            self.sensors[i + num_thermostat] = sensor('c02', numRows)

if __name__ == '__main__':
    s = sensor('thermostat')
