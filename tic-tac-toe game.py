# /////////////////// بسم الله ////////////////////

# import turtle
import random
from tkinter import *

wind = Tk()
wind.title(" - X O Game By MO - ")

# ]
def next_return(row, col):
    global player
    if game_buttons[row][col]["text"] == "" and check_winner() == False:
        if player == players[0]:
            game_buttons[row][col]["text"] = player

            if check_winner() == False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[0] + " wins !"))

            elif check_winner() == "tie":
                label.config(text=("Tie, No Winners!"))

        elif player == players[1]:
            game_buttons[row][col]["text"] = player

            if check_winner() == False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[1] + " wins !"))

            elif check_winner() == "tie":
                label.config(text=("Tie, No Winners!"))

# ]
def check_winner():
    for row in range(3):
        if (
            game_buttons[row][0]["text"]
            == game_buttons[row][1]["text"]
            == game_buttons[row][2]["text"]
            != ""
        ):
            game_buttons[row][0].config(bg="cyan")
            game_buttons[row][1].config(bg="cyan")
            game_buttons[row][2].config(bg="cyan")
            return True

    for col in range(3):
        if (
            game_buttons[0][col]["text"]
            == game_buttons[1][col]["text"]
            == game_buttons[2][col]["text"]
            != ""
        ):
            game_buttons[0][col].config(bg="cyan")
            game_buttons[1][col].config(bg="cyan")
            game_buttons[2][col].config(bg="cyan")
            return True

    if (
        game_buttons[0][0]["text"]
        == game_buttons[1][1]["text"]
        == game_buttons[2][2]["text"]
        != ""
    ):
        game_buttons[0][0].config(bg="cyan")
        game_buttons[1][1].config(bg="cyan")
        game_buttons[2][2].config(bg="cyan")
        return True

    elif (
        game_buttons[0][2]["text"]
        == game_buttons[1][1]["text"]
        == game_buttons[2][0]["text"]
        != ""
    ):
        game_buttons[0][2].config(bg="cyan")
        game_buttons[1][1].config(bg="cyan")
        game_buttons[2][0].config(bg="cyan")
        return True

    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_buttons[row][col].config(bg="red")
        return "tie"

    else:
        return False

# ]
def check_empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_buttons[row][col]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

# 4]
def restart():
    global player
    player = random.choice(players)
    label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            # game_buttons[row][col].config(text="",bg="gray")
            game_buttons[row][col].config(text="", bg="#F0F0F0")


# =========================================================
players = ["X", "O"]
player = random.choice(players)

game_buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(text=(player + " turn"), font=("consoles", 40))
label.pack(side="top")

restart_bottom = Button(text="restart", font=("consoles", 20), command=restart)
restart_bottom.pack(side="top")

buttons_frame = Frame(wind)
buttons_frame.pack()

for row in range(3):
    for col in range(3):
        game_buttons[row][col] = Button(
            buttons_frame,
            text="",
            font=("consoles", 50),
            width=5,
            height=2,
            command=lambda row=row, col=col: next_return(row, col),
        )
        game_buttons[row][col].grid(row=row, column=col)

wind.mainloop()