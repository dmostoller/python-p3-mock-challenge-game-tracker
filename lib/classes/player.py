from classes.result import Result


class Player:
    all = []

    def __init__(self, username):
        self.username = username

        Player.all.append(self)

        self._games_played = []
        self._results = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise Exception("Username must be a string beween 2-16 characters long")


    def results(self):
        return self._results
    
    def add_result(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        else:
            raise Exception("Result must be an instance of the Result class")
    
    results = property(results, add_result)

    def games_played(self):
        return self._games_played
    
    def add_game_played(self, new_game_played):
        from classes.game import Game
        if isinstance(new_game_played, Game):
            self._games_played.append(new_game_played)
        else:
            raise Exception("Game must be an instance of the Game class")

    def played_game(self, game):
        if game in self._results:    
            return True
        else:
            return False
    

    def num_times_played(self, game):
        num_played = {}
        for result in self._results:
            if game == result.game.title:
                if game not in num_played:
                    num_played[game] = 1
                else: 
                    num_played[game] += 1
                
                return num_played[game]
            else:
                return "None"

            

    @classmethod
    def highest_scored(cls, game):
        pass


    def __repr__(self):
        return f"Player - {self.username}"