from player import Player


class AIPlayer(Player):
    """This player should implement a heuristic along with a min-max and alpha
    beta search to """

    depth = 2
	
    def __init__(self):
        self.name = "Mettez ici le nom de votre IA"

    
    def getColumn(self, board):
        column = findBestColumn(self, board)
        return randomColumn(self, board) if column == -1 else column

    def randomColumn(self, board):
        columns = board.getPossibleColumns()
        if columns:
            return random.choice(columns)

    def findBestColumn(self, board):
        possibleColumns = board.getPossibleColumns()
        for column in possibleColumns:
            if isWinner(self, board, column):
                return column
            if isPreventLoser(self, board, column):
                return column
        return -1

    def isWinner(self, board, column):
        


    def isPreventLoser(self, board, column):
