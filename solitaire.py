from deck import Deck
from tableau import Tableau
from foundation import Foundation


class Solitaire:
    def __init__(self):
        self.deck = Deck()
        self.tableau = Tableau(self.deck)
        self.foundation = Foundation()

    def move_card_from_tableau_to_foundation(self, fundation_pile_number,
                                             tableau_pile_number, card):
        if self.foundation.is_valid_move(fundation_pile_number, card) and \
                    self.tableau.is_card_on_top(tableau_pile_number, card):
            self.foundation.add_card(fundation_pile_number, card)
            self.tableau.remove_card_on_top(tableau_pile_number, card)

            if self.foundation.is_game_won():
                print("You won!")

    def move_card_from_fundation_to_tableau(self, fundation_pile_number,
                                            tableau_pile_number, card):
        if self.tableau.is_valid_move(tableau_pile_number, card) and \
                    self.foundation.is_valid_move(fundation_pile_number, card):
            self.tableau.add_card(tableau_pile_number, card)
            self.foundation.remove_card(fundation_pile_number, card)
