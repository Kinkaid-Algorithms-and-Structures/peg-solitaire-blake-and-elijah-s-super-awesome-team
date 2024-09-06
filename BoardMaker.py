from operator import truediv
from tokenize import triple_quoted
from Peg import PegHole

class BoardMaker:
    def __init__(self):
        global board
        board = [["O"],
                 ["X", "X"],
                 ["X", "X", "X"],
                 ["X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X"]]
        tag_list = [1, 2, 3, 1, 4, 1, 2, 3, 2, 3, 1, 4, 1, 4, 1]
        place = 0
        row_counter = 0
        new_board = []
        for row in board:
            row_counter += 1
            col_counter = 0
            new_board.append([])
            #print(row[0])
            for spot in row:
                col_counter += 1
                new_board[row_counter - 1].append(PegHole(place, True, tag_list[place], row_counter, col_counter))
                print(place)
                place += 1
        new_board[0][0].filled = False
        board = new_board

    #def create_board(self, new_board):

    def make_board(self):
        print("        ", board[0][0].print(), "       ")
        print("      ", board[1][0].print(), " ", board[1][1].print(), "     ")
        print("    ", board[2][0].print(), " ", board[2][1].print(), " ", board[2][2].print(), "    ")
        print("  ", board[3][0].print(), " ", board[3][1].print(), " ", board[3][2].print(), " ", board[3][3].print(), "   ")
        print("", board[4][0].print(), " ", board[4][1].print(), " ", board[4][2].print(), " ", board[4][3].print(), " ", board[4][4].print())

    #def move(self, from_space, over_space, too_space):
     #   board[from_space] = "O"
      #  board[over_space] = "O"
       # board[too_space] = "X"

    def check_board(self) -> bool :
        number_of_xs = 0
        for i in range(len(board)):
            if board[i] == "X":
                number_of_xs = number_of_xs + 1
        if number_of_xs > 1:
            return False
        else:
            return True


    def get_board(self):
        return board




if __name__ == "__main__":
    board_maker = BoardMaker()
    board_maker.make_board()
