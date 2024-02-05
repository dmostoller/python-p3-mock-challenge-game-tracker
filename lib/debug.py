#!/usr/bin/env python3
# import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

# if __name__ == '__main__':
#     print("HELLO! :) let's debug :vibing_potato:")

#     ipdb.set_trace()

tetris = Game("Tetris")
pokemon = Game("Pokemon")
doom = Game("Doom")

dave = Player("Dave")
peter = Player("Peter")
beth = Player("Beth")

result1 = Result(dave, pokemon, 800)
result2 = Result(peter, pokemon, 500)
result3 = Result(beth, tetris, 4000)
result4 = Result(dave, doom, 100)
result5 = Result(peter, doom, 50)
result6 = Result(beth, tetris, 400)

print(dave.num_times_played("Doom"))