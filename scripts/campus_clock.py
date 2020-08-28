from campus import campus
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import json

class clock:

    def __init__(self, number_campuses, number_hours):
        start_time = time.time()
        self.campus = campus()
        inputData = self.loadData()
        self.age(inputData, number_hours)

        elapsed_time = time.time() - start_time
        print('ELAPSED TIME:\t{}'.format(elapsed_time))

        self.makeDict()

    # age the campus using input data as base
    def age(self, input_data, number_hours):
        for row_index, row in input_data.iterrows():
            if row_index < number_hours:
                self.campus.getOlder(row_index, input_data.iloc[row_index:(row_index + 1) , :])
            else:
                pass

    # read data in from raw_csv file
    def loadData(self):
        df = pd.read_csv('data/raw_data/AEP_hourly.csv', index_col=[0], parse_dates=[0])
        df['index'] = np.arange(len(df))
        df = df.set_index('index')
        return df

    def graphDF(self, df):
        color_pal = ["#F8766D", "#D39200", "#93AA00", "#00BA38", "#00C19F", "#00B9E3", "#619CFF", "#DB72FB"]
        df.plot(style='.', figsize=(15,5), color=color_pal[0], title='PJM East')
        plt.show()

    def makeDict(self):
        buildingDict = {}

        for building in self.campus.buildings:
            building_object = self.campus.buildings[building]
            building_id = building_object.id_num
            buildingDict[building_id] = {}
            buildingDict[building_id]['rooms'] = {}
            buildingDict[building_id]['corridors'] = {}

            for room in building_object.rooms:
                room_object = building_object.rooms[room]
                room_id = room_object.room_id
                buildingDict[building_id]['rooms'][room_id] = {}

                for sensor in room_object.sensors:
                    sensor_object = room_object.sensors[sensor]
                    meter_id = sensor_object.meter_id
                    buildingDict[building_id]['rooms'][room_id][meter_id] = {}
                    buildingDict[building_id]['rooms'][room_id][meter_id]['age'] = str(sensor_object.age)
                    buildingDict[building_id]['rooms'][room_id][meter_id]['deaths'] = str(sensor_object.deaths)
                    buildingDict[building_id]['rooms'][room_id][meter_id]['latest_ttl'] = int(sensor_object.ttl)

            for corridor in building_object.corridors:
                corridor_object = building_object.corridors[corridor]
                corridor_id = corridor_object.corridor_id
                buildingDict[building_id]['corridors'][corridor_id] = {}

                for sensor in corridor_object.sensors:
                    sensor_object = corridor_object.sensors[sensor]
                    meter_id = sensor_object.meter_id
                    buildingDict[building_id]['corridors'][corridor_id][meter_id] = {}
                    buildingDict[building_id]['corridors'][corridor_id][meter_id]['age'] = str(sensor_object.age)
                    buildingDict[building_id]['corridors'][corridor_id][meter_id]['deaths'] = str(sensor_object.deaths)
                    buildingDict[building_id]['corridors'][corridor_id][meter_id]['latest_ttl'] = str(sensor_object.ttl)
        print(buildingDict)

        with open('data/campus_snapshot.json', 'w') as f:
            json.dump(buildingDict, f)

if __name__ == '__main__':
    clock = clock(1, 10)
