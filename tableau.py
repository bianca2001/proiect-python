class Tableau:
    def __init__(self, deck):
        self.piles = []

        for i in range(7):
            self.piles.append(deck.getCards(i+1))
            self.piles[i][-1].flip()

    def is_valid_move(self, destination_pile_number, card):
        if self.piles[destination_pile_number] == []:
            print("Empty pile")
            if card.get_rank() != 13:
                print("Not a king")
                return False
            return True

        if not card.is_face_up():
            print("Not face up")
            return False

        first_card_destination = self.piles[destination_pile_number][-1]

        if first_card_destination.get_color() == card.get_color():
            print("Same color:", first_card_destination.get_color(),
                  card.get_color())
            return False

        if first_card_destination.get_rank() != card.get_rank() + 1:
            print("Not one less:", first_card_destination.get_rank(),
                  card.get_rank())
            return False

        return True

    def move_pile_to_pile(self, source_pile_number, destination_pile_number,
                          card_pos):
        source_pile = self.piles[source_pile_number]
        destination_pile = self.piles[destination_pile_number]
        if self.is_valid_move(destination_pile_number, source_pile[card_pos]):
            for j in range(card_pos, len(source_pile)):
                destination_pile.append(source_pile.pop(card_pos))
            if source_pile != [] and not source_pile[-1].is_face_up():
                source_pile[-1].flip()

    def is_card_on_top(self, pile_number, card):
        return self.piles[pile_number][-1] == card

    def remove_card_on_top(self, pile_number, card):
        self.piles[pile_number].pop()

    def add_card(self, pile_number, card):
        print("Trying to add card:", card, "to pile:", pile_number)
        print(card.rank)

        if self.is_valid_move(pile_number, card):
            self.piles[pile_number].append(card)
        else:
            print("Invalid move")

    def __getitem__(self, item):
        return self.piles[item]

    def __len__(self):
        return len(self.piles)

    def __str__(self):
        return str(self.piles)
