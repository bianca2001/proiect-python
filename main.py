import tkinter as tk
from solitaire import Solitaire
import functools
root = tk.Tk()
root.title("Solitaire")

card_height = 192
card_width = 120
game = Solitaire()
waste_pile_cards = game.deck.deal()
foundation_frame = None
board_frame = None


def draw_card(card, rank, suit, color, flipped=True):
    if not flipped:
        card.create_rectangle(2, 2, card_width - 2, card_height - 2,
                              fill="lightblue", outline="black")
        return
    card.create_rectangle(2, 2, card_width - 2, card_height - 2,
                          outline=color)
    card.create_text(15, 15, text=rank, font=("Arial", 14), fill=color)
    card.create_text(15, 30, text=suit, font=("Arial", 14), fill=color)


def create_cards():
    global board_frame
    global game

    if board_frame:
        board_frame.destroy()

    board_frame = tk.Frame(root)
    board_frame.place(relx=0.5, rely=0.98, anchor="s")
    board = tk.Canvas(board_frame, width=card_width * 7 + 50 * 8,
                      height=card_height + 45 * 13, bg="white",
                      highlightthickness=0)
    board.pack()
    piles = game.tableau
    for i in range(7):
        for j in range(len(piles[i])):
            card = tk.Canvas(board_frame, width=card_width, height=card_height,
                             bg="white", highlightthickness=0)
            card.bind("<Button-1>", on_drag_start)
            card.bind("<B1-Motion>", on_drag_motion)
            card.bind("<ButtonRelease-1>",
                      functools.partial(on_drop, pile=i, card_pos=j))
            card.place(x=i * (card_width + 50) + 50, y=j * 45)

            draw_card(card, piles[i][j].rank, piles[i][j].suit,
                      piles[i][j].get_color(), piles[i][j].is_face_up())


# Function to create foundation piles (simple rectangles)
def create_foundation():
    global foundation_frame
    global game
    foundation_frame = tk.Frame(root)
    foundation_frame.place(relx=0, rely=0, anchor="nw")

    for i in range(4):
        foundation_pile = tk.Canvas(foundation_frame, width=card_width,
                                    height=card_height, bg="white",
                                    highlightthickness=0)
        foundation_pile.grid(row=0, column=i, padx=20, pady=10)

        # Draw a rectangle for foundation pile
        if game.foundation.piles[i] == []:
            foundation_pile.create_rectangle(2, 2, card_width - 2,
                                             card_height - 2,
                                             outline="black")
        else:
            draw_card(foundation_pile,
                      game.foundation.piles[i][-1].rank,
                      game.foundation.piles[i][-1].suit,
                      game.foundation.piles[i][-1].get_color())

        foundation_pile.bind("<Button-1>", on_drag_start)
        foundation_pile.bind("<B1-Motion>", on_drag_motion)
        foundation_pile.bind("<ButtonRelease-1>",
                             functools.partial(on_drop, pile=i))


# Function to create stock and waste piles (simple rectangles)
def create_stock_waste():
    global waste_pile_cards
    stock_waste_frame = tk.Frame(root)
    stock_waste_frame.place(relx=1, rely=0, anchor="ne")

    stock_pile = tk.Canvas(stock_waste_frame, width=card_width,
                           height=card_height, bg="white",
                           highlightthickness=0)
    stock_pile.bind("<Button-1>", change_waste)
    stock_pile.grid(row=0, column=1, padx=20, pady=10)

    # Draw a rectangle for stock pile
    stock_pile.create_rectangle(2, 2, card_width - 2, card_height - 2,
                                outline="black")

    waste_pile_frame = tk.Frame(stock_waste_frame)
    waste_pile_frame.grid(row=0, column=0, padx=20, pady=10)
    waste_pile = tk.Canvas(waste_pile_frame, width=card_width + 2 * 45,
                           height=card_height, bg="white",
                           highlightthickness=0)
    waste_pile.grid(row=0, column=0)

    for i in range(len(waste_pile_cards)):
        card = tk.Canvas(waste_pile, width=card_width,
                         height=card_height, bg="white",
                         highlightthickness=0)
        card.place(x=i * 45, y=0)

        card.create_rectangle(2, 2, card_width - 2, card_height - 2,
                              outline="black")

        draw_card(card, waste_pile_cards[i].rank, waste_pile_cards[i].suit,
                  waste_pile_cards[i].get_color())

        if i == len(waste_pile_cards) - 1:
            card.bind("<Button-1>", on_drag_start)
            card.bind("<B1-Motion>", on_drag_motion)
            card.bind("<ButtonRelease-1>", on_drop)


def change_waste(event):
    global game
    global waste_pile_cards
    waste_pile_cards = game.deck.deal(waste_pile_cards)
    create_stock_waste()


drag_object = [None, None]


def on_drag_start(event):
    widget = event.widget
    widget.start_x = event.x
    widget.start_y = event.y


def on_drag_motion(event):
    dx = event.x - card_width / 2
    dy = event.y - card_height / 2
    event.widget.place(x=event.widget.winfo_x() + dx, y=event.widget.winfo_y()
                       + dy)
    event.widget.start_x = event.x
    event.widget.start_y = event.y


def solve_drop_on_foundation(event, pile=None, card_pos=None):
    global foundation_frame
    global game
    print("Maybe drop on foundation")

    if event.x_root > foundation_frame.winfo_rootx() + 4 * \
            (card_width + 20) + 60:
        print("Not in fundation pile")
        return

    destination_pile = None
    for i in range(4):
        x_range = (foundation_frame.winfo_rootx() + i * (card_width + 40),
                   foundation_frame.winfo_rootx() + (i + 1) *
                   (card_width + 40))

        if x_range[0] <= event.x_root <= x_range[1]:
            destination_pile = i
            break

    print("Destination pile:", destination_pile)

    if destination_pile is None:
        create_cards()
        return

    if card_pos is None:
        print("Trying to move card from waste to foundation")
        if game.foundation.is_valid_move(destination_pile,
                                         waste_pile_cards[-1]):
            game.foundation.add_card(destination_pile,
                                     waste_pile_cards[-1])
            waste_pile_cards.pop()
            create_stock_waste()
            create_foundation()
            create_cards()
            return
        create_cards()
        return

    if game.foundation.is_valid_move(destination_pile,
                                     game.tableau[pile][card_pos]):
        game.foundation.add_card(destination_pile,
                                 game.tableau[pile][card_pos])
        game.tableau.remove_card_on_top(pile, game.tableau[pile][card_pos])
        if game.tableau[pile] and not game.tableau[pile][-1].is_face_up():
            game.tableau[pile][-1].flip()
        create_foundation()
        create_cards()
        return

    create_cards()
    create_foundation()
    create_stock_waste()


def on_drop(event, pile=None, card_pos=None):
    global waste_pile_cards
    global game

    # Drop on foundation
    if event.y_root < board_frame.winfo_rooty():
        solve_drop_on_foundation(event, pile, card_pos)
        return

    # Drop on tableau
    destination_pile = None
    for i in range(7):
        x_range = (board_frame.winfo_rootx() + i * (card_width + 50) + 50,
                   board_frame.winfo_rootx() + (i + 1) * (card_width + 50) +
                   50)

        if x_range[0] <= event.x_root <= x_range[1]:
            destination_pile = i
            break

    print("Destination pile:", destination_pile)

    if destination_pile is None:
        create_cards()
        create_foundation()
        create_stock_waste()
        return

    print("Pile:", pile)
    if card_pos is None:
        print("Trying to move card from waste or fundation to tableau")

        if pile is not None:
            print("Trying to move pile", pile, "to pile", destination_pile)
            print("Card:", game.foundation.piles[pile][-1].rank,
                  game.foundation.piles[pile][-1].suit,
                  game.foundation.piles[pile][-1].get_color())
            if game.tableau.is_valid_move(destination_pile,
                                          game.foundation.piles[pile][-1]):
                game.tableau.add_card(destination_pile,
                                      game.foundation.piles[pile][-1])
                game.foundation.remove_card(pile)
            create_foundation()
            create_cards()
            return
        else:
            if game.tableau.is_valid_move(destination_pile,
                                          waste_pile_cards[-1]):
                game.tableau.add_card(destination_pile, waste_pile_cards[-1])
                waste_pile_cards.pop()
            create_stock_waste()
            create_cards()
            return

    game.tableau.move_pile_to_pile(pile, destination_pile,
                                   card_pos)
    create_cards()
    create_foundation()
    create_stock_waste()


# Create cards, foundation piles, stock, and waste piles
create_stock_waste()
create_cards()
create_foundation()


root.mainloop()
