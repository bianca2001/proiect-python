from card.py import Card
import random


class Deck:
    def __init__(self):
        self.cards = self.getNewDeck()

    def getNewDeck():
        new_deck = []

        for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for rank in range(1, 14):
                new_deck.append(Card(suit, rank))

        return new_deck

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
