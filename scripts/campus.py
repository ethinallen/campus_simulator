import numpy as np
from building import building

class campus:

    # initialize the sensor based on type and set age to 0
    def __init__(self):
        self.buildings = { }
        num_buildings = np.random.poisson(35, 1)[0]

        self.makeBuildings(num_buildings)

    # instantiate buildings
    def makeBuildings(self, num_buildings):
        for i in range(num_buildings):
            self.buildings[i] = building(i, 10)

    # iterate through time
    def getOlder(self, time, new_rows):

        for building in self.buildings:
            building_object = self.buildings[building]

            building_object.generate_power_consumption(time)

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
