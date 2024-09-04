import logging, datetime
from KinkaidDecorators import log_start_stop_method
from Peg import PegHole

logging.basicConfig(level=logging.INFO)  # simple version to the output console
# logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file cNode = Tuple[int, T]

class PegSolitaireRunner:
    def __init__(self):
        logging.info("Initializing.")
        global moving
        moving = None
        global board
        board = [["0"],
                 ["1","2"],
                 ["3","4","5"],
                 ["6","7","8","9"],
                 ["10","11","12","13","14",]]
        tag_list = [1,2,3,1,4,1,2,3,2,3,1,4,1,4]
        place = 0
        row_counter = 0
        new_board = []
        for row in board:
            row_counter += 1
            col_counter = 0
            new_board.append([])
           # print(row[0])
            for spot in row: #These aren't being added to the board, Not sure why
                print(spot)
                col_counter += 1
                new_board[row_counter-1].append(PegHole(place, True, tag_list[place], row_counter, col_counter))
            place += 1
        board = new_board
        print(board)
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
        self.check_legality(origin, end)
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
