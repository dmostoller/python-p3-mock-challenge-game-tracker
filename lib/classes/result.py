class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        self.__class__.all.append(self)

    @property
    def player(self):
        return self._player
        
    @player.setter
    def player(self, value):
        from classes.player import Player
        if isinstance(value, Player):
            self._player = value
        else:
            raise Exception("Player must be an instance of the Player class")
        
    @property
    def game(self):
        return self._game 
    
    @game.setter
    def game(self, value):
        from classes.game import Game
        if isinstance(value, Game):
            self._game = value
        else:
            raise Exception("Game must be an instance of the game class")
        
    @property
    def score(self):
        return self._score 
    
    @score.setter
    def score(self, value):
        if not hasattr(self, '_score') and isinstance(value, int) and 1 <= value <= 5000:
            self._score = value
        else:
            raise Exception("Score must be an integer between 1 and 5000")
        
    
    def __repr__(self):
        return f"{self.game} {self.player} Score - {self.score}"