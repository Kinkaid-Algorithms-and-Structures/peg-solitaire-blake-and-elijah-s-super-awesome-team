from operator import truediv
from tokenize import triple_quoted

board = ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]

class BoardMaker:
    def __init__(self):
        print("board:")


    def make_board(self):
        print("        ", board[0], "       ")
        print("      ", board[1], " ", board[2], "     ")
        print("    ", board[3], " ", board[4], " ", board[5], "    ")
        print("  ", board[6], " ", board[7], " ", board[8], " ", board[9], "   ")
        print("", board[10], " ", board[11], " ", board[12], " ", board[13], " ", board[14])

    def move(self, from_space, over_space, too_space):
        board[from_space] = "O"
        board[over_space] = "O"
        board[too_space] = "X"

    def check_board(self) -> bool :
        number_of_xs = 0
        for i in range(len(board)):
            if board[i] == "X":
                number_of_xs = number_of_xs + 1
        if number_of_xs > 1:
            return False
        else:
            return True






if __name__ == "__main__":
    board_maker = BoardMaker()
    board_maker.make_board()
