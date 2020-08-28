import numpy as np
from building import building
import pandas as pd

class campus:

    # initialize the sensor based on type and set age to 0
    def __init__(self):
        self.df = pd.DataFrame()
        self.buildings = { }

        self.entries = []

        # num_buildings = np.random.poisson(35, 1)[0]
        num_buildings = 1

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

            # s = (
            #     f"{row['Datetime']},"
            #     f"{building_object.building_id},"
            #     f"building_object.previous_power_consumption\n"
            # )

            entry = {
                'Datetime'  : [row['Datetime']],
                'PSID'      : [building_object.building_id],
                'Value'     : [building_object.previous_power_consumption]
            }


            row_df = pd.DataFrame(entry)
            self.entries.append(row_df)


            # for room in building_object.rooms:
            #     room_object = building_object.rooms[room]
            #     for sensor in room_object.sensors:
            #         sensor_object = room_object.sensors[sensor]
            #         sensor_object.getOlder()

    def write_output_csv(self):
        self.df = pd.concat(self.entries)
        # self.df.to_csv


if __name__ == '__main__':
    c = campus()

    for building in c.buildings:
        for room in building:
            print(room)
