from main import *
import numpy as np


class AI(Game):

    def __init__(self):

        super().__init__()

        self.depth = 0

    def max(self):
        max_score = -2
        cell_x = 0
        cell_y = 0
        choice_pool = []

        # Checking game state
        self.check_if_end()

        # End states of recursive function. When algorythm comes to an end of a game tree branch, function returns a
        # value accordingly to game state (X win, O win, tie)
        if self.game_state == 'X is win!':
            return -1, 0, 0
        if self.game_state == 'O is win!':
            return 1, 0, 0
        if self.game_state == 'Board is full!':
            return 0, 0, 0

        # Recursive function
        if self.game_state == 'In progress':
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col] == '-':
                        self.board[row][col] = 'O'
                        self.depth += 1
                        branch_score = self.min()
                        self.depth -= 1
                        if branch_score[0] > max_score:
                            max_score = branch_score[0]
                            cell_x = row
                            cell_y = col
                            if self.depth == 0:
                                choice_pool.clear()
                                choice_pool.append((max_score, cell_x, cell_y))
                        if branch_score[0] == max_score:
                            if self.depth == 0:
                                cell_x = row
                                cell_y = col
                                choice_pool.append((max_score, cell_x, cell_y))
                        self.board[row][col] = '-'
                        self.game_state = 'In progress'
        if self.depth == 0:
            return choice_pool[np.random.randint(len(choice_pool))]
        return max_score, cell_x, cell_y

    def min(self):
        min_score = 2
        cell_x = 0
        cell_y = 0

        # Checking game state
        self.check_if_end()

        # End states of recursive function. When algorythm comes to an end of a game tree branch, function returns a
        # value accordingly to game state (X win, O win, tie)
        if self.game_state == 'X is win!':
            return -1, 0, 0
        if self.game_state == 'O is win!':
            return 1, 0, 0
        if self.game_state == 'Board is full!':
            return 0, 0, 0

        # Recursive function
        if self.game_state == 'In progress':
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col] == '-':
                        self.board[row][col] = 'X'
                        self.depth += 1
                        branch_score = self.max()
                        self.depth -= 1
                        if branch_score[0] < min_score:
                            min_score = branch_score[0]
                            cell_x = row
                            cell_y = col
                        self.board[row][col] = '-'
                        self.game_state = 'In progress'
        return min_score, cell_x, cell_y

    def change_cell_state_ai(self, row, col):
        if self.turn == 0:
            if self.board[row - 1][col - 1] == '-':
                self.board[row-1][col-1] = "X"
        else:
            self.board[self.max()[1]][self.max()[2]] = 'O'
