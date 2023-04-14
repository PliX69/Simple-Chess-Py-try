import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Chess")

board = []
for i in range(8):
    row = []
    for j in range(8):
        button = tk.Button(root, width=5, height=2)
        button.grid(row=i, column=j)
        row.append(button)
    board.append(row)

White_pawn  =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\white_pawn.png")
White_knight  =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\white_knight.png")
White_rook  =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\white_rook.png")
White_bishop  =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\white_bishop.png")
White_queen  =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\white_queen.png")
White_king =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\white_king.png")
black_pawn  =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\lack_pawn.png")
black_knight  =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\lack_knight.png")
black_rook  =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\lack_rook.png")
black_bishop  =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\lack_bishop.png")
black_queen  =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\lack_queen.png")
black_king =  Image.open("D:\Website\Instantnudeln.de\GPT\Pictures\lack_king.png")

White_pawn = White_pawn.resize(button["width"], button["height"])
White_knight = White_knight.resize(button["width"], button["height"])
White_rook = White_rook.resize(button["width"], button["height"])
White_bishop = White_bishop.resize(button["width"], button["height"])
White_queen = White_queen.resize(button["width"], button["height"])
White_king = White_king.resize(button["width"], button["height"])
black_pawn = black_pawn.resize(button["width"], button["height"])
black_knight = black_knight.resize(button["width"], button["height"])
black_rook = black_rook.resize(button["width"], button["height"])
black_bishop = black_bishop.resize(button["width"], button["height"])
black_queen = black_queen.resize(button["width"], button["height"])
black_king = black_king.resize(button["width"], button["height"])


photoimg = ImageTk.PhotoImage(White_pawn)
photoimg = ImageTk.PhotoImage(White_knight)
photoimg = ImageTk.PhotoImage(White_rook)
photoimg = ImageTk.PhotoImage(White_bishop)
photoimg = ImageTk.PhotoImage(White_queen)
photoimg = ImageTk.PhotoImage(White_king)
photoimg = ImageTk.PhotoImage(black_pawn)
photoimg = ImageTk.PhotoImage(black_knight)
photoimg = ImageTk.PhotoImage(black_rook)
photoimg = ImageTk.PhotoImage(black_bishop)
photoimg = ImageTk.PhotoImage(black_queen)
photoimg = ImageTk.PhotoImage(black_king)


pieces = {}
pieces["wp"] = White_pawn
pieces["wr"] = White_rook
pieces["wn"] = White_knight
pieces["wb"] = White_bishop
pieces["wq"] = White_queen
pieces["wk"] = White_king
pieces["bp"] = black_pawn
pieces["br"] = black_rook
pieces["bn"] = black_knight
pieces["bb"] = black_bishop
pieces["bq"] = black_queen
pieces["bk"] = black_king


start_position = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]

for i in range(8):
    for j in range(8):
        if start_position[i][j] != "":
            board[i][j].config(image=ImageTk.PhotoImage(pieces[start_position[i][j]]))

root.mainloop()
