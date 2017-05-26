import random
import time
play_again = True
difficulty = 'easy'
min_max = random.randrange(1000000000,2000000000)
guessed_number_right = False
player_guess = False

while play_again:
    print("This program will think of a number, you may then attempt to guess it.")

    valid_difficulty = False
    while valid_difficulty == False:
        difficulty = input("Would you like easy, medium, or hard mode? ")
        difficulty = difficulty.lower()
        print("You have chosen " + difficulty)

        if difficulty == 'easy':
            min_max = random.randrange(1000000000,2000000000)
            valid_difficulty = True
            print("I'll think of a number between 1000000000 and 2000000000")
        elif difficulty == 'medium':
            min_max = random.randrange(1000000000,3000000000)
            print("I'll think of a number between 1000000000 and 3000000000")
            valid_difficulty = True
        elif difficulty == 'hard':
            min_max = random.randrange(1000000000,4000000000)
            print("I'll think of a number between 1000000000 and 4000000000")
            valid_difficulty = True
        else:
            print("Non-valid input")



    print("Okay, im thinking of a number...")
    time.sleep(6)
    print(min_max)
    print("Alright, I got one, go ahead and guess ")
    guessed_number_right = False

    while guessed_number_right == False:
        player_guess = int(input())
        if player_guess == min_max:
            guessed_number_right = True
        elif player_guess >min_max:
            print("Your number is too high, guess again")
        elif player_guess < min_max:
            print("Your number is too low, guess again")

    print("You guessed the number right Would you like to play again?")

    valid_answer = False
    while valid_answer == False:
        response = input()
        if response in ['yes', 'Yes']:
            print("Alright, lets do it")
            valid_answer = True
        elif response in ['no', 'No']:
            print("Goodbye then.")
            valid_answer = True
            play_again = False
