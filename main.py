import tkinter as tk
root = tk.Tk()
root.title("Solitaire")

def create_cards():
    for i in range(7):
        for j in range(i + 1):

            card = tk.Canvas(root, width=50, height=80, bg="white", highlightthickness=0)
            card.grid(row=j + 4, column=i, padx=5, pady=5)

            card.create_rectangle(2, 2, 48, 78, outline="black")

            rank = "A"
            suit = "♥" 
            card.create_text(25, 40, text=rank, font=("Arial", 16))
            card.create_text(25, 60, text=suit, font=("Arial", 16))

def create_foundation():
    for i in range(4):
        foundation_pile = tk.Canvas(root, width=50, height=80, bg="white", highlightthickness=0)
        foundation_pile.grid(row=0, column=i, padx=5, pady=5)

        # Draw a rectangle for foundation pile
        foundation_pile.create_rectangle(2, 2, 48, 78, outline="black")

def create_stock_waste():
    stock_pile = tk.Canvas(root, width=50, height=80, bg="white", highlightthickness=0)
    stock_pile.grid(row=0, column=8, padx=(0, 5), pady=5, sticky="en")

    stock_pile.create_rectangle(2, 2, 48, 78, outline="black")

    waste_pile = tk.Canvas(root, width=50, height=80, bg="white", highlightthickness=0)
    waste_pile.grid(row=0, column=9, padx=5, pady=5, sticky="e")

    waste_pile.create_rectangle(2, 2, 48, 78, outline="black")

create_cards()
create_foundation()
create_stock_waste()

root.mainloop()
