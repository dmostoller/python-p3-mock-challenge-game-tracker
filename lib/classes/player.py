
class Player:

    all = []

    def __init__(self, username):
        self.username = username

        self.__class__.all.append(self)

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
        from classes.result import Result
        return [result for result in Result.all if result.player == self]    

    def games_played(self):
        return list(set([result.game for result in self.results()]))

    def played_game(self, game):
        return game in self.games_played()    

    
    def num_times_played(self, game):
       return len([result for result in self.results() if result.game == game])
    
    @classmethod
    def highest_scored(cls, game):
        max_player = None
        max_score = 0
        for player in cls.all:
            if player.played_game(game):
                if game.average_score(player) > max_score:
                    max_player = player
                    max_score = game.average_score(player)
        return max_player


    def __repr__(self):
        return f"Player - {self.username}"