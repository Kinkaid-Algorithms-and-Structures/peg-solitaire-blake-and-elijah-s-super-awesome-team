class PegHole:
    def __init__(self,place,filled,tag,row,col):
        self.place=place
        self.filled=filled
        self.tag=tag
        self.row=row
        self.col=col
        pass


    def print(self):
        if self.filled:
            return "X"
        else:
            return "O"


'''
        Pegs holes to need to be an object with these values
        Place:0-14
        Filled:Boolean
        Tag:1-4 as modeled
        row: row of hole
        col: column of peg
    '''