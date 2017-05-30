class Person:


    def __init__(self):
        self.name = 'Conner'

    def __init__(self, assigned_name):
        self.name = assigned_name

    def print_name(self):
        print(self.name)

    def __str__(self):
        return 'This person is named {}'.format(self.name)

    def __repr__(self):
        return self.__str__()


conner = Person()

conner.phone = '8584446174'

conner.print_name()

print(conner.phone)


print(conner)

print([conner])
