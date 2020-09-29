import numpy as np
from building import building
import pandas as pd
import numpy as np
import datetime
import time
import dateutil.parser
from dateutil.parser import parse
import os

class campus:

    # initialize the sensor based on type and set age to 0
    def __init__(self):
        self.df = pd.DataFrame()
        self.buildings = { }

        self.entries = []

        # num_buildings = np.random.poisson(10, 1)[0]
        num_buildings = 10

        self.makeBuildings(num_buildings)

    # instantiate buildings
    def makeBuildings(self, num_buildings):
        for i in range(num_buildings):
            self.buildings[i] = building(i)

    # age every building 1 unit of time
    def getOlder(self, row):
        for building in self.buildings:
            building_object = self.buildings[building]

            building_object.generate_power_consumption(row['AEP_MW'])

            epoch_time = time.mktime(datetime.datetime.strptime(row['Datetime'], "%Y-%m-%d %H:%M:%S").timetuple())
            entry = [int(epoch_time), 0, int(building_object.building_id), int(building_object.previous_power_consumptions[-1]), -1, -1, -1]

            self.entries.append(entry)

            for room in building_object.rooms:
                room_object = building_object.rooms[room]
                for i, sensor in enumerate(room_object.sensors):
                    sensor_object = room_object.sensors[sensor]
                    reading = sensor_object.getOlder()
                    entry = [epoch_time, 1, int(building_object.building_id), 0, int(room_object.room_id), i, int(reading)]

                    self.entries.append(entry)

            for corridor in building_object.corridors:
                corridor_object = building_object.corridors[corridor]
                for sensor in corridor_object.sensors:
                    sensor_object = corridor_object.sensors[sensor]
                    sensor_object.getOlder()

                    reading = sensor_object.getOlder()
                    # id = building_object.building_id * 10000 + room_object.room_id * 100 + i
                    entry = [int(epoch_time), 1, int(building_object.building_id), 1, int(corridor_object.corridor_id), i, int(reading)]

                    self.entries.append(entry)


    def write_output_csv(self):
        try:
            np.set_printoptions(suppress=True)
            # np_array = np.array([self.entries])
            np_array = np.array([np.array(xi) for xi in self.entries])
            # print(np_array)
            np.savetxt('./data/processed_data/output.csv', np_array, delimiter=',', fmt='%d')
            # np.savetxt("./data/processed_data/output.csv", np_array, delimiter=",")
            os.system('say "Finished writing"')
        except Exception as e:
            print('Error: {}'.format(e))


if __name__ == '__main__':
    c = campus()

    for building in c.buildings:
        for room in building:
            print(room)
