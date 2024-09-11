import sys
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
        print("         0  ")
        print("       1   2 ")
        print("     3   4   5")
        print("   6   7   8   9")
        print(" 10  11  12  13  14")
        tag_list = [1, 2, 3, 1, 4, 1, 2, 3, 2, 3, 1, 4, 1, 4, 1]
        place = 0
        row_counter = 0
        new_board = []
        for row in board:
            row_counter += 1
            col_counter = 0
            new_board.append([])
            for spot in row:
                col_counter += 1
                new_board[row_counter - 1].append(PegHole(place, True, tag_list[place], row_counter, col_counter))
                place += 1
        #new_board[0][0].filled = False
        board = new_board

    #def create_board(self, new_board):

    def make_board(self):
        print(f"         {board[0][0].print()}        ")
        print(f"       {board[1][0].print()}   {board[1][1].print()}     ")
        print(f"     {board[2][0].print()}   {board[2][1].print()}   {board[2][2].print()}     ")
        print(f"   {board[3][0].print()}   {board[3][1].print()}   {board[3][2].print()}   {board[3][3].print()}    ")
        print(f" {board[4][0].print()}   {board[4][1].print()}   {board[4][2].print()}   {board[4][3].print()}   {board[4][4].print()}")

    def move(self, origin, del_row, del_col, end):
        organ = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].row == del_row and board[i][j].col == del_col:
                    organ = board[i][j]
        origin.filled = False
        organ.filled = False
        end.filled = True


    def check_board(self) -> bool :
        number_of_xs = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].filled:
                    number_of_xs = number_of_xs + 1
        if number_of_xs > 1:
            return False
        else:
            print('You Won, Congrats!')
            sys.ext
            return True


    def get_board(self):
        return board




if __name__ == "__main__":
    board_maker = BoardMaker()
    board_maker.make_board()
