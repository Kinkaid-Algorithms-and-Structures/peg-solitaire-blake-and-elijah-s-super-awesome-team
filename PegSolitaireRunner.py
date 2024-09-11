from BoardMaker import BoardMaker
from KinkaidDecorators import log_start_stop_method
from BoardMaker import BoardMaker


class PegSolitaireRunner:
    def __init__(self):
        global board_maker
        board_maker = BoardMaker()
        global board
        board = board_maker.get_board()
        self.ask_move()


    # add any code you want to set up variables for the game.
    
    @log_start_stop_method
    def play_game(self):  # note: this is complaining (grey underline) that it could be static because it doesn't use
        # any variables or methods from "self." Once you do, it will stop pestering you about it.
        pass
    def ask_move(self):
        board_maker.make_board()
        origin = None
        end = None
        try:
            origin = int(input("What peg do you want to move?"))
        except:
            print("Please enter an integer")
        try:
            end = int(input("Where do you want the peg to go?"))
        except:
            print("Please enter an integer")
        global organ
        organ = None
        global ender
        ender = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].place == origin:
                    organ = board[i][j]
                elif board[i][j].place == end:
                    ender = board[i][j]
        self.check_legality(organ, ender)
    def check_legality(self,origin,end):
        #if origin.tag == end.tag:
        if True:
            if (origin.row - end.row) == -2 and (origin.col - end.col) == -2: #diag southeast check
                board_maker.move(origin,(origin.row+1),(origin.col+1),end)
                print("moved")
            elif (origin.row - end.row) == 2 and (origin.col - end.col) == 2: #diag northwest check
                board_maker.move(origin,(origin.row-1),(origin.col-1),end)
                print("moved")
            elif (origin.row - end.row) == 2 and (origin.col - end.col) == 0: #up check
                board_maker.move(origin,(origin.row-1),origin.col,end)
                print("moved")
            elif (origin.row - end.row) == - 2 and (origin.col - end.col) == 0:  #down check
                board_maker.move(origin,(origin.row+1),origin.col,end)
                print("moved")
            elif (origin.row - end.row) == 0 and (origin.col - end.col) == -2: #right check
                board_maker.move(origin,origin.row,(origin.col+1),end)
                print("moved")
            elif (origin.row - end.row) == 0 and (origin.col - end.col) == 2: #left check
                board_maker.move(origin,origin.row,(origin.col-1),end)
                print("moved")
            else:
                #move is illegal
                print("That move seems to be illegal \n try again!")
                self.ask_move()
                pass
        else:
            print("That move seems to be illegal \n try again!")
            self.ask_move()
            pass
        board_maker.check_board()
        self.ask_move()


if __name__ == "__main__":
    game = PegSolitaireRunner()
    game.play_game()
