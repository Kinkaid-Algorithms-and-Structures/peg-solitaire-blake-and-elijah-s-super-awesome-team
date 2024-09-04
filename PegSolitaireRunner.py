import logging, datetime

from BoardMaker import BoardMaker
from KinkaidDecorators import log_start_stop_method
#from Peg import PegHole
from BoardMaker import BoardMaker

logging.basicConfig(level=logging.INFO)  # simple version to the output console
# logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file cNode = Tuple[int, T]

class PegSolitaireRunner:
    def __init__(self):
        logging.info("Initializing.")
        board_maker = BoardMaker()
        global board
        board = board_maker.get_board()
        self.ask_move()
       # print(board[0][0])


    # add any code you want to set up variables for the game.
    
    @log_start_stop_method
    def play_game(self):  # note: this is complaining (grey underline) that it could be static because it doesn't use
        # any variables or methods from "self." Once you do, it will stop pestering you about it.
        pass
    def ask_move(self):
        origin = input("What peg do you want to move?")
        end = input("Where do you want the peg to go?")
        global organ
        global ender
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].place == origin:
                    organ = board[i][j]
                elif board[i][j].place == end:
                    ender = board[i][j]
        self.check_legality(organ, ender)
    def check_legality(self,origin,end):
        '''
        TO DO, Origin and End need to convert to their objects



        '''



        # move(from,end)
        '''
        Requirements for this to work
        Board needs to be a list of lists as modeled above
        Pegs holes to need to be an object with these values
        Place:0-14
        Filled:Boolean
        Tag:1-4 as modeled
        row: row of hole
        col: column of peg
        '''

        if origin.tag == end.tag and (origin.row - end.row) + (origin.col - end.col) <= 2: #checks if the move is legal from start to end
            if (origin.row - end.row) == -2 and (origin.col - end.col) == 2: #diag southeast check
                board.move(origin,[origin.row+1][origin.col+1],end)
            elif (origin.row - end.row) == 2 and (origin.col - end.col) == -2: #diag northwest check
                board.move(origin,[origin.row-1][origin.col-1],end)
            elif (origin.row - end.row) == 2 and (origin.col - end.col) == 0: #down check
                board.move(origin,[origin.row+1][origin.col],end)
            elif (origin.row - end.row) == - 2 and (origin.col - end.col) == 0:  #up check
                board.move(origin, [origin.row-1][origin.col], end)
            elif (origin.row - end.row) == 0 and (origin.col - end.col) == -2: #right check
                board.move(origin,[origin.row][origin.col+1],end)
            elif (origin.row - end.row) == 0 and (origin.col - end.col) == 2: #left check
                board.move(origin, [origin.row-1][origin.col-1], end)
            else:
                #move is illegal
                print("That move seems to be illegal /n try again!")
                ask_move()
                pass
        else:
            print("That move seems to be illegal /n try again!")
            ask_move()
            pass

if __name__ == "__main__":
    game = PegSolitaireRunner()
    game.play_game()
