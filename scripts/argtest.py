class testClass():

    def __init__(self, a, b, *args):
        print(a)
        print(b)

        for arg in args:
            print("ARG:\t{}".format(arg))


if __name__ == '__main__':
    t = testClass('a', 'b', 'c', 'd', 'e', 'f', 'g')
    
