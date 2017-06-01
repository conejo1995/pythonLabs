class Car:
    number_of_wheels = 4



    def __init__(self, color = 'red', number_of_doors = 4):
        self.color = color
        self.number_of_doors = number_of_doors

    def print_car(self):
        print("The color is {}.".format(self.color))
        print("There are {} doors.".format(self.number_of_doors))
        print("There are {} wheels.".format(self.number_of_wheels))

    def honk(self):
        print('honk')
