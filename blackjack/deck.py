from random import shuffle
from random import randrange
class Deck:
    possible_suits = ['Spade', 'Club', 'Heart', 'Diamond']
    possible_ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    deck_of_cards = []
    card_number_index = 0

    def __init__(self):
        for suit in self.possible_suits:
            for rank in self.possible_ranks:
                m = Card(suit,rank)
                self.deck_of_cards.append(m)
        self.shuffle_deck()
        # for card in self.deck_of_cards:
        #     print(card.rank + " " + card.suit)

    def cut_deck(self):
        cut = randrange[:len(deck_of_cards)]
        self.deck_of_cards = self.deck_of_cards[cut:] + self.deck_of_cards[:cut]

    def shuffle_deck(self):
        shuffle(self.deck_of_cards)

    def draw_card(self):
        temp_card =self.deck_of_cards.pop()
        return temp_card
class Card:
    suit = ''
    rank = ''
    def __init__(self, suit = 'Spade', rank = 'Ace'):
        self.suit = suit
        self.rank = rank
