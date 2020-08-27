from campus import campus

#
class clock:

    def __init__(self, number_buildings, number_hours):
        self.c = campus(number_buildings)
        self.age(number_hours)

    def age(self, number_hours):
        for i in range(number_hours):
            self.c.getOlder(i)

if __name__ == '__main__':
    clock = clock(5, 100)
