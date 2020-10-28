import numpy as np
from building import building
import pandas as pd
import numpy as np
import datetime
import time
import dateutil.parser
from dateutil.parser import parse
import os

import meerschaum as mrsm

class campus:

    # initialize the sensor based on type and set age to 0
    def __init__(self, numRows, *attrs):

        self.df = pd.DataFrame()
        self.buildings = { }

        self.entries = { }
        self.metrics = {
            'power' : [],
            'temperature' : []
        }

        if attrs:
            for buildingID in attrs[0]['buildings']:
                building_attributes = {'id': buildingID, 'info' : attrs[0]['buildings'][buildingID]}
                self.buildings[buildingID] = building(np.int64(buildingID), numRows, building_attributes)
                self.entries[buildingID] = []

        else:
            # num_buildings = np.random.poisson(10, 1)[0]
            num_buildings = 5

            self.makeBuildings(num_buildings, numRows)

    # instantiate buildings
    def makeBuildings(self, num_buildings, numRows):
        for i in range(num_buildings):
            self.buildings[i] = building(i, numRows)
            self.entries[i] = []

    # age every building 1 unit of time
    def getOlder(self, row, index):
        for building in self.buildings:
            building_object = self.buildings[building]

            reading = building_object.generate_power_consumption(row['AEP_MW'], index)

            epoch_time = time.mktime(datetime.datetime.strptime(row['Datetime'], "%Y-%m-%d %H:%M:%S").timetuple())
            entry = [np.int64(epoch_time), np.int64(building_object.id), np.int64(reading)]

            self.metrics['power'].append(entry)

            for room in building_object.rooms:
                room_object = building_object.rooms[room]
                for i, sensor in enumerate(room_object.sensors):
                    sensor_object = room_object.sensors[sensor]
                    deviation = sensor_object.getOlder(index)
                    entry = [int(epoch_time), int(building_object.id), int(room_object.id), int(sensor_object.id), np.int64(deviation)]
                    self.metrics['temperature'].append(entry)

            for corridor in building_object.corridors:
                corridor_object = building_object.corridors[corridor]
                for i, sensor in enumerate(corridor_object.sensors):
                    sensor_object = corridor_object.sensors[sensor]

                    deviation = sensor_object.getOlder(index)
                    entry = [int(epoch_time), int(building_object.id), int(corridor_object.id), int(sensor_object.id), np.int64(deviation)]
                    self.metrics['temperature'].append(entry)

    def makePipe(self):
        pipe = mrsm.Pipe('sim', 'power', str(building))
        pipe.parameters = {
            'columns' : {
                'datetime'  : 'epochTime',
                'id'        : 'sensorid'
            }
        }

        pipe.register(debug=True)
        return pipe

    '''
        def writeDB(self):
            - write power from building
            - write every sensor output
    '''

if __name__ == '__main__':
    c = campus()
    c.makePipe()
