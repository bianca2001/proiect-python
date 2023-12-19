from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []

        for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, previous_cards=[]):
        next_cards = []

        for i in range(3):
            next_cards.append(self.cards.pop())

        self.cards.append(previous_cards)
        return next_cards

    def getCards(self, number_of_cards):
        new_cards = []

        for i in range(number_of_cards):
            new_cards.append(self.cards.pop())

        return new_cards
