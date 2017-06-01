from deck import Deck
from deck import Card
class Hand:
    cards_in_hand = []

    def __init__(self, current_deck):
        self.cards_in_hand = []
        self.cards_in_hand.append(current_deck.draw_card())
        self.cards_in_hand.append(current_deck.draw_card())
        # for card in self.cards_in_hand:
        #     print(card.rank + " " + card.suit)

    def add_card(self, current_deck):
        self.cards_in_hand.append(current_deck.draw_card())

    def show_hand(self):
        for card in self.cards_in_hand:
            print(card.rank + " of " + card.suit + "'s")




def create_new_hand(temp_deck):
    temp_hand = Hand()
    i = 0
    while i < 3:
        suit = input("Input a card suit ")
        rank = input("Input a card rank ")
        if suit in temp_deck.possible_suits:
            if rank in temp_deck.possible_ranks:
                temp_hand.add_card(Card(suit, rank))
                i = i + 1
    return temp_hand
