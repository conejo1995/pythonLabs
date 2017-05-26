def greeting_to_person(n, phone):
    name = "Chris"
    print('Hello {}'.format(n) + " " + phone)

name = input("What is your name? ")
number = input("What is your number? ")
greeting_to_person(name, number)
