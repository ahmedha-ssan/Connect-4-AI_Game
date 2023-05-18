from board import Board
import numpy as np

class AlphaBeta:
    def __init__(self, depth):
        self.depth = depth

    def get_move(self, board):
        value, move = self.alphabeta(board, self.depth, -np.inf, np.inf, True)
        return move

    def alphabeta(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.game_over:
            return self.evaluate(board), None

        if maximizing_player:
            value = -np.inf
            best_move = None
            for col in range(7):
                if board.board[0][col] == 0:
                    board_copy = Board()
                    board_copy.board = np.copy(board.board)
                    board_copy.turn = board.turn
                    board_copy.game_over = board.game_over
                    board_copy.play(col)
                    new_value, _ = self.alphabeta(board_copy, depth-1, alpha, beta, False)
                    if new_value > value:
                        value = new_value
                        best_move = col
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break
            return value, best_move
        else:
            value = np.inf
            best_move = None
            for col in range(7):
                if board.board[0][col] == 0:
                    board_copy = Board()
                    board_copy.board = np.copy(board.board)
                    board_copy.turn = board.turn
                    board_copy.game_over = board.game_over
                    board_copy.play(col)
                    new_value, _ = self.alphabeta(board_copy, depth-1, alpha, beta, True)
                    if new_value < value:
                        value = new_value
                        best_move = col
                    beta = min(beta, value)
                    if alpha >= beta:
                        break
            return value, best_move

    def evaluate(self, board):
        score = 0
        for r in range(6):
            for c in range(7):
                if board.board[r][c] == 1:
                    score += self.get_score(board, r, c, 1)
                elif board.board[r][c] == 2:
                    score -= self.get_score(board, r, c, 2)
        return score

    def get_score(self, board, row, col, player):
        score = 0
        # check horizontal
        left = max(col-3, 0)
        right = min(col+3, 6)
        for c in range(left, right-2):
            window = board.board[row][c:c+4]
            score += self.get_window_score(window, player)
        # check vertical
        bottom = max(row-3, 0)
        top = min(row+3, 5)
        for r in range(bottom, top-2):
            window = board.board[r:r+4, col]
            score += self.get_window_score(window, player)
        # check diagonal
        bottom_left = (max(row-3, 0), max(col-3, 0))
        top_right = (min(row+3, 5), min(col+3, 6))
        for r in range(bottom_left[0], top_right[0]-2):
            for c in range(bottom_left[1], top_right[1]-2):
                window = [board.board[r+i][c+i] for i in range(4)]
                score += self.get_window_score(window, player)
        top_left = (max(row-3, 0), min(col+3, 6))
        bottom_right = (min(row+3, 5), max(col-3, 0))
        for r in range(bottom_right[0], min(top_left[0]+1, 3)):
            for c in range(bottom_right[1], top_left[1]+2):
                window = [board.board[r+i][c-i] for i in range(4)]
                score += self.get_window_score(window, player)
        return score

    def get_window_score(self, window, player):
        opponent = 2 if player == 1 else 1
        if np.count_nonzero(np.array(window) == player)==4:
            return 100
        elif np.count_nonzero(np.array(window) == player)==3 and np.count_nonzero(np.array(window) == 0)==1:
            return 5
        elif np.count_nonzero(np.array(window) == player)==2 and np.count_nonzero(np.array(window) == 0)==2:
            return 2
        elif np.count_nonzero(np.array(window) == opponent)==3 and np.count_nonzero(np.array(window) == 0)==1:
            return -4
        else:
            return 0