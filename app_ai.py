from minimax import *
import tkinter as tk
import tkinter.messagebox as tkm


def start():
    # Game initialization
    global game
    game = AI()
    visualize_board()
    Button_MakeAMove['state'] = tk.NORMAL


def visualize_board():
    for label in labels:
        label.destroy()
    for row in range(len(game.board)):
        for col in range(len(game.board[0])):
            label = tk.Label(text=game.board[row][col])
            label.grid(row=row+2, column=col)
            labels.append(label)


def move():
    if game.game:
        if x.get() == 0 or y.get() == 0 or x.get() > 3 or y.get() > 3:
            tkm.showinfo("Error!", "Out of game boundaries!")
            return
        else:
            game.change_cell_state_ai(x.get(), y.get())
            visualize_board()
            game.check_if_end()

    if game.game_state == 'X is win!' or game.game_state == 'O is win!' or game.game_state == 'Board is full!':
        game.game = False
    else:
        game.pass_turn()

    if game.game == False:
        Button_MakeAMove['state'] = tk.DISABLED
        gstatus = tk.Label(text=game.game_state)
        gstatus.grid(row=5, column=0, columnspan=4)


def quit_game():
    game.game = False
    root.destroy()


root = tk.Tk()
root.title('Tic-Tac-Toe')
root.geometry('300x130')

# Variables
x = tk.IntVar()
y = tk.IntVar()
labels = []


# Spinboxes
Spinbox_X = tk.Spinbox(root, textvariable=x, width=10)
Spinbox_X.grid(row=1, column=1)
Spinbox_Y = tk.Spinbox(root, textvariable=y, width=10)
Spinbox_Y.grid(row=1, column=2)

# Buttons
Button_Start = tk.Button(root, text='Start a Game', command=start)
Button_Start.grid(row=0, column=0, rowspan=2)
Button_MakeAMove = tk.Button(root, text='Make a Move', command=move, state=tk.DISABLED)
Button_MakeAMove.grid(row=0, column=1, columnspan=2)
Button_Quit = tk.Button(root, text='Quit Game', command=quit_game)
Button_Quit.grid(row=0, column=3, rowspan=2)

root.mainloop()