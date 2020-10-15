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
    def __init__(self, numRows):
        self.df = pd.DataFrame()
        self.buildings = { }

        self.entries = { }
        self.metrics = {
            'power' : [],
            'temperature' : []
        }

        # num_buildings = np.random.poisson(10, 1)[0]
        num_buildings = 10

        # self.makePipe()
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
            entry = [int(epoch_time), 0, int(building_object.id), int(reading), -1, -1, -1]

            '''
                epochTime,isSensor,buildingid,buildingpowerreading,roomcorrobjectid,sensorid,reading
            '''

            self.metrics['power'].append(entry)


            for room in building_object.rooms:
                room_object = building_object.rooms[room]
                for i, sensor in enumerate(room_object.sensors):
                    sensor_object = room_object.sensors[sensor]
                    deviation = sensor_object.getOlder(index)
                    entry = [epoch_time, 1, int(building_object.id), -1, int(room_object.id), i, int(deviation)]
                    self.metrics['temperature'].append(entry)

            for corridor in building_object.corridors:
                corridor_object = building_object.corridors[corridor]
                for i, sensor in enumerate(corridor_object.sensors):
                    sensor_object = corridor_object.sensors[sensor]

                    deviation = sensor_object.getOlder(index)
                    entry = [int(epoch_time), 1, int(building_object.id), -2, int(corridor_object.id), i, int(deviation)]
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
