import numpy as np
from building import building

class campus:

    # initialize the sensor based on type and set age to 0
    def __init__(self, numBuildings):
        self.buildings = { }

        self.makeBuildings(numBuildings)

    # instantiate buildings
    def makeBuildings(self, numBuildings):
        for i in range(numBuildings):
            self.buildings[i] = building(i, 4, 10)

    # iterate through time
    def getOlder(self, time):

        for building in self.buildings:
            building_object = self.buildings[building]

            building_object.generate_power_consumption(time)

            for room in building_object.rooms:
                room_object = building_object.rooms[room]
                for sensor in room_object.sensors:
                    sensor_object = room_object.sensors[sensor]
                    sensor_object.getOlder()

if __name__ == '__main__':
    c = campus(2)

    for building in c.buildings:
        for room in building:
            print(room)
