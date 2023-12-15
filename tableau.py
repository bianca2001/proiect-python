from card.py import Card
from deck.py import Deck


class Tableau:
    def __init__(self):
        self.piles = []

    def add_piles(self, deck):
        for i in range(7):
            self.piles.append(deck.getCards(i+1))