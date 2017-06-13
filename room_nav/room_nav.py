from room import Room
from character import Character



def battle(player, npc):
    fighting = True
    print("You are now battling " + npc.name)
    while fighting:
        user_input = input("What would you like to do?")
        if user_input == 'fight':
            npc.take_damage(player.attack)
            print(npc.name + " took " + str(player.attack) + ' damage')
            if npc.health <= 0:
                print("You have defeated " + npc.name)
                fighting = False


def players_room(player, player_room):
    input_strings = []
    player_room.things_in_room()
    while True:
        user_input = input("What would you like to do? ")
        user_input = user_input.lower()
        input_strings = user_input.split()
        if 'down' in input_strings and 'stairs' in input_strings or 'downstairs' in input_strings:
            return 2


def players_home(player, player_home):
    input_strings = []
    player_home.things_in_room()
    while True:
        user_input = input()
        user_input = user_input.lower()
        input_strings = user_input.split()
        if 'talk' in input_strings and player_home.characters[0].name.lower() in input_strings:
            player_home.characters[0].speak()
        if 'fight' in input_strings and player_home.characters[0].name.lower() in input_strings:
            battle(player, player_home.characters[0])



user_input = 1
turns = 0
stranger = Character('Stranger')
player = Character()
player_room = Room("This is your room, you recognize all the things in it as being your own. There is a staircase in this room leading downstairs.")
player_home = Room("This is your living room, there is a door leading outside and a staircase leading up stairs to your room.")
player_home.add_character(stranger)
while True:
    if user_input ==1:
        user_input = players_room(player, player_room)
    elif user_input ==2:
        user_input = players_home(player, player_home)
