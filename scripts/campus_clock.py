from campus import campus
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import json

'''
    - need to make sure that reporting is int
    - make a csv for each building metric
    -
'''

class clock:

    def __init__(self, number_campuses):
        start_time = time.time()


        self.campus = campus()
        inputData = self.loadData()

        self.age(inputData)

        self.campus.write_output_csv()

        self.writeDict(self.makeDict())

        elapsed_time = time.time() - start_time
        # print('ELAPSED TIME:\t{}'.format(elapsed_time))

    # age the campus using input data as base
    def age(self, input_data):
        for row_index, row in input_data.iterrows():
            self.campus.getOlder(row)
        # print('DONE AGING')

    # read data in from raw_csv file
    def loadData(self):
        df = pd.read_csv('./data/raw_data/AEP_hourly.csv')
        df['index'] = np.arange(len(df))
        df.set_index('index')
        return df

    def graphDF(self):
        color_pal = ["#F8766D", "#D39200", "#93AA00", "#00BA38", "#00C19F", "#00B9E3", "#619CFF", "#DB72FB"]
        self.inputData.plot(style='.', figsize=(15,5), color=color_pal[0], title='Data')
        plt.show()

    # make dictionary of all of the aspects of campus; returns dictionary
    def makeDict(self):
        buildingDict = { }

        for building in self.campus.buildings:
            building_object = self.campus.buildings[building]
            building_id = building_object.building_id
            buildingDict[building_id] = { }
            buildingDict[building_id]['power_readings'] = building_object.previous_power_consumptions
            buildingDict[building_id]['rooms'] = { }
            buildingDict[building_id]['corridors'] = { }

            for room in building_object.rooms:
                room_object = building_object.rooms[room]
                room_id = room_object.room_id
                buildingDict[building_id]['rooms'][room_id] = { }

                for sensor in room_object.sensors:
                    sensor_object = room_object.sensors[sensor]
                    meter_id = sensor_object.meter_id
                    buildingDict[building_id]['rooms'][room_id][meter_id] = { }
                    buildingDict[building_id]['rooms'][room_id][meter_id]['age'] = str(sensor_object.age)
                    buildingDict[building_id]['rooms'][room_id][meter_id]['deaths'] = str(sensor_object.deaths)
                    buildingDict[building_id]['rooms'][room_id][meter_id]['latest_ttl'] = int(sensor_object.ttl)

            for corridor in building_object.corridors:
                corridor_object = building_object.corridors[corridor]
                corridor_id = corridor_object.corridor_id
                buildingDict[building_id]['corridors'][corridor_id] = { }

                for sensor in corridor_object.sensors:
                    sensor_object = corridor_object.sensors[sensor]
                    meter_id = sensor_object.meter_id
                    buildingDict[building_id]['corridors'][corridor_id][meter_id] = { }
                    buildingDict[building_id]['corridors'][corridor_id][meter_id]['age'] = str(sensor_object.age)
                    buildingDict[building_id]['corridors'][corridor_id][meter_id]['deaths'] = str(sensor_object.deaths)
                    buildingDict[building_id]['corridors'][corridor_id][meter_id]['latest_ttl'] = str(sensor_object.ttl)
        return buildingDict

    def writeDict(self, buildingDict):
        with open('./data/campus_snapshot.json', 'w+') as f:
            json.dump(buildingDict, f, indent=4, sort_keys=True)

if __name__ == '__main__':
    clock = clock(2)
