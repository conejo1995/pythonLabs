import hand
from deck import Deck
from deck import Card
from time import sleep

def start_new_game_or_quit():
    valid_response = False
    while valid_response == False:
        user_input = input("Would you like to start a new game, or quit?(new, quit) ")
        user_input = user_input.lower()
        if user_input == 'new':
            valid_response = True
        if user_input == 'quit':
            quit()

def score_hand(some_hand):
    possible_ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    actual_values = [1,2,3,4,5,6,7,8,9,10,10,10,10]
    score = 0
    for card in some_hand.cards_in_hand:
        index = 0
        for po_rank in possible_ranks:
            if card.rank == po_rank:
                score = score + actual_values[index]
            index = index + 1
    if 'Ace' in some_hand.cards_in_hand and score + 10 <= 21:
        score = score + 10
    return score

def hit_or_stay(player_hand):
    running = True
    while running:
        user_input = input("Hit or stay?(hit, stay) ")
        if user_input =='hit':
            return 'hit'
        elif user_input == 'stay':
            return 'stay'
        else:
            pass

def dealer_turn(dealer_hand, player_hand):
    running = True
    while running:
        if score_hand(dealer_hand) <= 17 or score_hand(player_hand) > score_hand(dealer_hand):
            return "hit"
        else:
            return "stay"

def winner(player_hand, dealer_hand):
    if score_hand(player_hand) > score_hand(dealer_hand):
        print("You Win!!!")
    if score_hand(player_hand) < score_hand(dealer_hand):
        print("You Lose!!!")
    if score_hand(player_hand) == score_hand(dealer_hand):
        print("Tie!!!")

running = True
while running:

    start_new_game_or_quit()
    game_deck = Deck()
    player_hand = hand.Hand(game_deck)
    dealer_hand = hand.Hand(game_deck)

    game_going = True
    player = True
    print("You have: ")
    player_hand.show_hand()
    while player and game_going:

        response = hit_or_stay(player_hand)
        if response == 'hit':
            player_hand.add_card(game_deck)
            print("You have: ")
            player_hand.show_hand()
        elif response == 'stay':
            player = False
        if score_hand(player_hand) > 21:
            print('Bust!')
            player = False
            game_going = False
        elif score_hand(player_hand) == 21:
            print('You got 21, you win!')
            player = False
            game_going = False

    dealer = True
    if game_going:
        print("Dealer has: ")
        dealer_hand.show_hand()
    while dealer and game_going:

        response = dealer_turn(dealer_hand, player_hand)
        sleep(3)
        if response == 'hit':
            print("The dealer has decided to hit")
            dealer_hand.add_card(game_deck)
            print("Dealer has: ")
            dealer_hand.show_hand()
        elif response == 'stay':
            print("The dealer has decided to stay")
            dealer = False
        if score_hand(dealer_hand) > 21:
            print('Dealer busts, you win!')
            player = False
            game_going = False
        elif score_hand(dealer_hand) == 21:
            print('Dealer got 21, dealer wins!')
            player = False
            game_going = False

    if game_going:
        winner(player_hand, dealer_hand)
