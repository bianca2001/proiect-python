import tkinter as tk
root = tk.Tk()
root.title("Solitaire")

card_height = 192
card_width = 120


def draw_card(card, rank, suit):
    card.create_rectangle(2, 2, card_width - 2, card_height - 2,
                          outline="black")
    card.create_text(20, 20, text=rank, font=("Arial", 14))
    card.create_text(20, 40, text=suit, font=("Arial", 14))


def create_cards():
    board_frame = tk.Frame(root)
    board_frame.place(relx=0.5, rely=0.98, anchor="s")
    board = tk.Canvas(board_frame, width=card_width * 7 + 50 * 8,
                      height=card_height + 45 * 13, bg="white",
                      highlightthickness=0)
    board.pack()
    for i in range(7):
        for j in range(i + 1):

            card = tk.Canvas(board_frame, width=card_width, height=card_height,
                             bg="white", highlightthickness=0)
            card.place(x=i * (card_width + 50) + 50, y=j * 45)

            card.create_rectangle(2, 2, card_width - 2, card_height - 2,
                                  outline="black")

            draw_card(card, "A", "♥")


# Function to create foundation piles (simple rectangles)
def create_foundation():
    foundation_frame = tk.Frame(root)
    foundation_frame.place(relx=0, rely=0, anchor="nw")

    for i in range(4):
        foundation_pile = tk.Canvas(foundation_frame, width=card_width,
                                    height=card_height, bg="white",
                                    highlightthickness=0)
        foundation_pile.grid(row=0, column=i, padx=20, pady=10)

        # Draw a rectangle for foundation pile
        foundation_pile.create_rectangle(2, 2, card_width - 2, card_height - 2,
                                         outline="black")


# Function to create stock and waste piles (simple rectangles)
def create_stock_waste():
    stock_waste_frame = tk.Frame(root)
    stock_waste_frame.place(relx=1, rely=0, anchor="ne")

    stock_pile = tk.Canvas(stock_waste_frame, width=card_width,
                           height=card_height, bg="white",
                           highlightthickness=0)
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

    for i in range(3):
        card = tk.Canvas(waste_pile, width=card_width,
                         height=card_height, bg="white",
                         highlightthickness=0)
        card.place(x=i * 45, y=0)
        card.create_rectangle(2, 2, card_width - 2, card_height - 2,
                              outline="black")

        draw_card(card, "A", "♥")


# Create cards, foundation piles, stock, and waste piles
create_stock_waste()
create_cards()
create_foundation()


root.mainloop()
