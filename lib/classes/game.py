
class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not hasattr(self, '_title') and isinstance(new_title, str) and 0 < len(new_title):
            self._title = new_title
        else:
            raise Exception("Title must be a string greater than 0 characters, and cannot be changed once set.")

    def results(self):
        from classes.result import Result        
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results()]))
        
    def average_score(self, player):
        player_scores = [result.score for result in self.results() if result.player == player]
        if player_scores:
            return sum(player_scores) / len(player_scores)


    def __repr__(self):
        return f"Game - {self.title}"