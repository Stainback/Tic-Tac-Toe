# Step 1 - write a working prototype of Tic-Tac-Toe game with a hot seat multiplayer
# --> make a move --> check if win --> pass a move to opponent -->
#                                  --> win
# Step 2 - write a Minimax algorythm realization for the game (recursion depth is a rate of AI difficulty)
# Step 3 - write a small app for the game

class Game:

    def __init__(self):
        self.game = True
        self.turn = 0
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.game_state = 'In progress'

    def change_cell_state(self, row, col):
        if self.board[row-1][col-1] == '-':
            self.board[row-1][col-1] = "X" if self.turn == 1 else "O"
            self.pass_turn()

    def pass_turn(self):
        self.turn = 1 if self.turn == 0 else 0

    def check_if_end(self):
        # check if board is filled
        full_cells_counter = 0
        for row in self.board:
            for col in row:
                if col != '-':
                    full_cells_counter += 1
        if full_cells_counter == 9:
            self.game_state = 'Board is full!'
            return

        # check rows
        for row in self.board:
            if row == ['X', 'X', 'X']:
                self.game_state = 'X is win!'
                return
            if row == ['O', 'O', 'O']:
                self.game_state = 'O is win!'
                return
        # check columns
        board_transposed = [[], [], []]
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                board_transposed[col].append(self.board[row][col])
        for row in board_transposed:
            if row == ['X', 'X', 'X']:
                self.game_state = 'X is win!'
                return
            if row == ['O', 'O', 'O']:
                self.game_state = 'O is win!'
                return
        # check diagonals
        diagonals = ([self.board[0][0], self.board[1][1], self.board[2][2]],
                [self.board[0][2], self.board[1][1], self.board[2][0]])
        for d in diagonals:
            if d == ['X', 'X', 'X']:
                self.game_state = 'X is win!'
                return
            if d == ['O', 'O', 'O']:
                self.game_state = 'O is win'
                return

    def visualize_board(self):
        for row in self.board:
            for col in row:
                print(col, end=' ')
            print('\n')
        print('\n')
