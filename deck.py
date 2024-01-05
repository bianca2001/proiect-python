from card import Card
import random
import time


class Deck:
    def __init__(self):
        self.cards = []
        self.used_cards = []

        for suit in ["♥", "♦", "♠", "♣"]:
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
        print(len(self.cards))

    def shuffle(self):
        random.seed(int(time.time()))
        random.shuffle(self.cards)

    def deal(self, previous_cards=[]):
        self.used_cards.extend(previous_cards)
        next_cards = []

        if len(self.cards) == 0:
            self.cards = self.used_cards
            self.used_cards = []

        for i in range(min(3, len(self.cards))):
            aux = self.cards.pop(0)
            aux.flip()
            next_cards.append(aux)

        print(next_cards)
        return next_cards

    def getCards(self, number_of_cards):
        new_cards = []

        for i in range(number_of_cards):
            new_cards.append(self.cards.pop())

        return new_cards

    def __getitem__(self, item):
        return self.cards[item]
