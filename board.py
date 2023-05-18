from PIL import ImageGrab
import pyautogui
import numpy as np

# YOU MAY NEED TO CHANGE THESE VALUES BASED ON YOUR SCREEN SIZE
LEFT = 555
TOP = 260
RIGHT = 1300
BOTTOM = 900

EMPTY = 0
RED = 1
BLUE = 2


class Board:
    EMPTY = 0
    RED = 1
    BLUE = 2
    def __init__(self) -> None:
        self.board = [[EMPTY for i in range(7)] for j in range(6)]
        self.game_over = False
        self.turn = 1

    def print_grid(self, grid):
        print("#############################################\n")
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY:
                    print("*", end=" \t")
                elif grid[i][j] == RED:
                    print("R", end=" \t")
                elif grid[i][j] == BLUE:
                    print("B", end=" \t")
            print("\n")
        print("#############################################\n")

    def _convert_grid_to_color(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == (255, 255, 255):
                    grid[i][j] = EMPTY
                elif grid[i][j][2] <= 50:
                    grid[i][j] = RED
                elif grid[i][j][2] >= 190:
                    grid[i][j] = BLUE
        return grid

    def _get_grid_cordinates(self):
        startCord = (50, 55)
        cordArr = []
        for i in range(0, 7):
            for j in range(0, 6):
                x = startCord[0] + i * 115
                y = startCord[1] + j * 112
                cordArr.append((x, y))
        return cordArr

    def _transpose_grid(self, grid):
        return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    def _capture_image(self):
        image = ImageGrab.grab()
        cropedImage = image.crop((LEFT, TOP, RIGHT, BOTTOM))
        return cropedImage

    def _convert_image_to_grid(self, image):
        pixels = [[] for i in range(7)]
        i = 0
        for index, cord in enumerate(self._get_grid_cordinates()):
            pixel = image.getpixel(cord)
            if index % 6 == 0 and index != 0:
                i += 1
            pixels[i].append(pixel)
        return pixels

    def _get_grid(self):
        cropedImage = self._capture_image()
        pixels = self._convert_image_to_grid(cropedImage)
        #cropedImage.show()
        grid = self._transpose_grid(pixels)
        return grid

    def _check_if_game_end(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY and self.board[i][j] != EMPTY:
                    return True
        return False

    def get_game_grid(self):
        game_grid = self._get_grid()
        new_grid = self._convert_grid_to_color(game_grid)
        is_game_end = self._check_if_game_end(new_grid)
        self.board = new_grid
        return (self.board, is_game_end)

    def select_column(self, column):
        pyautogui.click(
            self._get_grid_cordinates()[column][1] + LEFT,
            self._get_grid_cordinates()[column][0] + TOP,
        )

    def play(self, col):
        if self.game_over:
            print("Game is over. Please start a new game.")
            return False , _,_

        if col < 0 or col > 6:
            print("Invalid move. Please choose a column between 0 and 6.")
            return False ,_,_

        if self.board[0][col] != 0:
            print("Column is full. Please choose another column.")
            return False,_,_

        row = 5
        while self.board[row][col] != 0:
            row -= 1

        self.board[row][col] = self.turn

        if self.check_win(row, col):
            self.game_over = True
          #  print(f"Player {self.turn} wins!")
        elif self.check_draw():
            self.game_over = True
        #    print("Game is a draw.")
        else:
            self.turn = 2 if self.turn == 1 else 1
        

        return True ,row,col

    def check_win(self, row, col):
        player = self.board[row][col]
        # check horizontal
        for c in range(4):
            if col-c >= 0 and self.board[row][col-c:col-c+4].tolist() == [player]*4:
                return True
        # check vertical
        if row <= 2 and self.board[row:row+4, col].tolist() == [player]*4:
            return True
        # check diagonal
        for r in range(3):
            if col-r >= 0 and row+r <= 2 and self.board[row+r:row+r+4, col-r:col-r+4].diagonal().tolist() == [player]*4:
                return True
            if col+r <= 6 and row+r <= 2 and np.fliplr(self.board[row+r:row+r+4, col-r:col-r+4]).diagonal().tolist() == [player]*4:
                return True
        return False

    def check_draw(self):
        return np.count_nonzero(self.board == 0) == 0
