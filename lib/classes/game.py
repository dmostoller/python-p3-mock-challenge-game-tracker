from classes.result import Result


class Game:
    def __init__(self, title):
        self.title = title

        self._players = []
        self._results = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not hasattr(self, 'title') and isinstance(new_title, str) and 0 < len(new_title):
            self._title = new_title
        else:
            raise Exception("Title must be a string greater than 0 characters, and cannot be changed once set.")

    
    def results(self):
        return self._results
    
    def add_result(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        else:
            raise Exception("Result must be an instance of the Result class")
    
    results = property(results, add_result)


    def players(self):
        return self._players
    
    def add_player(self, new_player=None):
        from classes.player import Player
        if isinstance(new_player, Player):
            self._players.append(new_player)
        else:
            raise Exception("Player must be an instance of the Player class")
        

    def average_score(self, player):
        pass

    def __repr__(self):
        return f"Game - {self.title}"