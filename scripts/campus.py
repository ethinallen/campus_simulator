import numpy as np
from building import building
import pandas as pd
import numpy as np
import datetime
import time


class campus:

    # initialize the sensor based on type and set age to 0
    def __init__(self):
        self.df = pd.DataFrame()
        self.buildings = { }

        self.entries = []

        num_buildings = np.random.poisson(10, 1)[0]

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

            entry = [epoch_time, int(building_object.building_id), int(building_object.previous_power_consumption)]

            self.entries.append(entry)

            for room in building_object.rooms:
                room_object = building_object.rooms[room]
                for sensor in room_object.sensors:
                    sensor_object = room_object.sensors[sensor]
                    sensor_object.getOlder()

    def write_output_csv(self):
        np_array = np.array(self.entries)
        np.savetxt("data/processed_data/output.csv", np_array, delimiter=",")

if __name__ == '__main__':
    c = campus()

    for building in c.buildings:
        for room in building:
            print(room)
