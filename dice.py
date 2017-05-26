from random import randint

number_of_dice = int(input("How many dice would you like to roll?"))
sides_on_dice = int(input("How many sides do the dice have?"))

c = 1

while c <= number_of_dice:
    print("Die number " + str(c) + " is a " + str(randint(1,sides_on_dice)))
    c = c+1
