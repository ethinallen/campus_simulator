import numpy as np
from building import building
import pandas as pd

class campus:

    # initialize the sensor based on type and set age to 0
    def __init__(self):
        self.df = pd.DataFrame()
        self.buildings = { }
        num_buildings = np.random.poisson(35, 1)[0]

        self.makeBuildings(num_buildings)

    # instantiate buildings
    def makeBuildings(self, num_buildings):
        for i in range(num_buildings):
            self.buildings[i] = building(i)

    # iterate through time
    def getOlder(self, row):
        for building in self.buildings:
            building_object = self.buildings[building]

            building_object.generate_power_consumption(row['AEP_MW'])

            entry = {
                'Datetime'  : [row['Datetime']],
                'PSID'      : [building_object.building_id],
                'Value'     : [building_object.previous_power_consumption]
            }

            row_df = pd.DataFrame(entry)
            self.df = self.df.append(row_df)


            for room in building_object.rooms:
                room_object = building_object.rooms[room]
                for sensor in room_object.sensors:
                    sensor_object = room_object.sensors[sensor]
                    sensor_object.getOlder()

if __name__ == '__main__':
    c = campus()

    for building in c.buildings:
        for room in building:
            print(room)
