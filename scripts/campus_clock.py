from campus import campus

from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
import json
import os

try:
    import meerschaum as mrsm
    print('IMPORTED Meerschaum')
except:
    print("\n\nFAILED TO IMPORT MEERSCHAUM!\n\n")

class clock:

    # not doing anything with the number of campuses yet
    def __init__(self, number_campuses):
        start_time = time.time()

        num_args = len(sys.argv)

        if num_args > 1:
            if sys.argv[1] == '-l':
                snapshot = self.loadSnapshot()
                inputData = self.loadData()
                numRows = len(inputData.index)
                self.campus = campus(numRows, snapshot)

        else:
            inputData = self.loadData().iloc[:5000]
            numRows = len(inputData.index)

            self.campus = campus(numRows)
            self.age(inputData)

        # self.write_output()
        self.writeDB()

        self.writeSnapshot(self.makeSnapshot())

        elapsed_time = time.time() - start_time
        print('ELAPSED TIME:\t{}'.format(elapsed_time))

    # age the campus using input data as base
    def age(self, input_data):
        for index, row in input_data.iterrows():
            self.campus.getOlder(row, index)
            ''' Brainstorming with Bennett :)
            self.campus.write()
            '''

    # read data in from raw_csv file
    def loadData(self):
        df = pd.read_csv('./data/raw_data/AEP_hourly.csv')
        df['index'] = np.arange(len(df))
        df.set_index('index')
        return df

    def loadSnapshot(self):
        print('LOADING SNAPSHOT')
        with open("./data/campus_snapshot.json", "r") as f:
            snapshot = json.load(f)
        return snapshot

    def graphDF(self):
        color_pal = ["#F8766D", "#D39200", "#93AA00", "#00BA38", "#00C19F", "#00B9E3", "#619CFF", "#DB72FB"]
        self.inputData.plot(style='.', figsize=(15,5), color=color_pal[0], title='Data')
        plt.show()

    # make snapshot of the state of the simulation
    def makeSnapshot(self):
        snapshot = { }

        snapshot['time'] = 1
        snapshot['buildings'] = {}

        for building in self.campus.buildings:
            building_object = self.campus.buildings[building]
            building_id = building_object.id
            s_building_id = str(building_object.id)
            snapshot['buildings'][s_building_id] = { }
            snapshot['buildings'][s_building_id]['stdev'] = building_object.stdev
            snapshot['buildings'][s_building_id]['adjustment'] = building_object.adjustment
            snapshot['buildings'][s_building_id]['rooms'] = { }
            snapshot['buildings'][s_building_id]['corridors'] = { }

            for room in building_object.rooms:
                room_object = building_object.rooms[room]
                room_id = room_object.id
                s_room_id = str(room_id)
                snapshot['buildings'][s_building_id]['rooms'][s_room_id] = { }

                for sensor in room_object.sensors:
                    sensor_object = room_object.sensors[sensor]
                    meter_id = sensor_object.id
                    s_meter_id = str(meter_id)
                    snapshot['buildings'][s_building_id]['rooms'][s_room_id][s_meter_id] = { }
                    snapshot['buildings'][s_building_id]['rooms'][s_room_id][s_meter_id]['age'] = sensor_object.age
                    snapshot['buildings'][s_building_id]['rooms'][s_room_id][s_meter_id]['latest_ttl'] = sensor_object.ttl
                    snapshot['buildings'][s_building_id]['rooms'][s_room_id][s_meter_id]['replacement_wait'] = sensor_object.replacement_wait

            for corridor in building_object.corridors:
                corridor_object = building_object.corridors[corridor]
                corridor_id = corridor_object.id
                s_corridor_id = str(corridor_id)
                snapshot['buildings'][s_building_id]['corridors'][s_corridor_id] = { }

                for sensor in corridor_object.sensors:
                    sensor_object = corridor_object.sensors[sensor]
                    meter_id = sensor_object.id
                    s_meter_id = str(meter_id)
                    snapshot['buildings'][s_building_id]['corridors'][s_corridor_id][s_meter_id] = { }
                    snapshot['buildings'][s_building_id]['corridors'][s_corridor_id][s_meter_id]['age'] = sensor_object.age
                    snapshot['buildings'][s_building_id]['corridors'][s_corridor_id][s_meter_id]['latest_ttl'] = sensor_object.ttl
                    snapshot['buildings'][s_building_id]['corridors'][s_corridor_id][s_meter_id]['replacement_wait'] = sensor_object.replacement_wait
        return snapshot

    # write the snapshot to a file
    def writeSnapshot(self, snapshot):
        with open('./data/campus_snapshot.json', 'w+') as f:
            json.dump(snapshot, f, indent=4)

    def write_output(self):
        print('Writing output csv...')
        try:
            power_filename = './data/processed_data/power.csv'
            temperature_filename = './data/processed_data/temperature.csv'

            np.set_printoptions(suppress=True)
            np_array = np.array([np.array(xi) for xi in self.campus.metrics['power']])

            np.savetxt(power_filename, np_array, delimiter=',', fmt='%d', header="epochTime,isSensor,buildingid,buildingpowerreading,roomcorrobjectid,sensorid,reading")

            np_array = np.array([np.array(xi) for xi in self.campus.metrics['temperature']])

            np.savetxt(temperature_filename, np_array, delimiter=',', fmt='%d', header="epochTime,isSensor,buildingid,buildingpowerreading,roomcorrobjectid,sensorid,reading")

        except Exception as e:
            print('Error: {}'.format(e))

    def writeDB(self):
        np.set_printoptions(suppress=True)
        power_array = np.array([np.array(xi) for xi in self.campus.metrics['power']])
        temperature_array = np.array([np.array(xi) for xi in self.campus.metrics['temperature']])

        powerDF = pd.DataFrame(data=power_array, columns=["epochTime","buildingid","reading"])
        temperatureDF = pd.DataFrame(data=temperature_array, columns=["epochTime","buildingid","roomcorrobjectid","sensorid","reading"])


        powerDF['datetime'] = pd.to_datetime(powerDF['epochTime'], unit='s')
        temperatureDF['datetime'] = pd.to_datetime(temperatureDF['epochTime'], unit='s')
        temperatureDF['reading'] = temperatureDF['reading'].astype(np.int64)
        temperatureDF['epochTime'] = temperatureDF['epochTime'].astype(np.int64)
        temperatureDF['buildingid'] = temperatureDF['buildingid'].astype(np.int64)
        temperatureDF['roomcorrobjectid'] = temperatureDF['roomcorrobjectid'].astype(np.int64)
        temperatureDF['sensorid'] = temperatureDF['sensorid'].astype(np.int64)
        print(temperatureDF.dtypes)

        powerPipe = mrsm.Pipe('sim', 'power', mrsm_instance='sql:mrsm_server')
        temperaturePipe = mrsm.Pipe('sim', 'temperature', mrsm_instance='sql:mrsm_server')

        powerPipe.sync(powerDF)
        temperaturePipe.sync(temperatureDF, debug=True)

if __name__ == '__main__':
    clock = clock(2)
