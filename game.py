class Game():
    def __init__(self, InterfaceClass, BoardClass, players):
        # Interface
        self.interface = InterfaceClass()

        # Board
        self.board = BoardClass(self.interface.getBoard())

        self.players = players
        self.history = []

        # Set interface for all players
        for player in self.players:
            player.interface = self.interface


    
    def loop(self):
        gameState = None
        # For every player
        for player in self.players:
            # Make a move
            self.history.append(player.makeMove(self.board))
            # Break the loop if the game is over
            gameState = self.board.getGameState()
            if gameState != None:
                break
        return gameState == None

    def end(self):
        self.interface.endGame(self.board, self.board.getGameState())
        

