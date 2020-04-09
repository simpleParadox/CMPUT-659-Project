from Player import Player
import random
from Game import Game
from DSL import DSL


class ScriptComb2(Player):

    def __init__(self):
        self._id = 1002
        self._strategies = ['DSL.isSmaller(a, 0 , Game.getRack() )',
                            'DSL.isCardBetweenNumbers(a, 39 , 26 , 0 )',
                            'DSL.isBigger(a, 3 , Game.getRack() )',
                            'DSL.isSmaller(a, 4 , Game.getRack() )',
                            'DSL.isCardBetweenNumbers(a, 9 , 13 , 0 )',
                            'DSL.isSmaller(a, 3 , Game.getRack() )',
                            'DSL.isCardBetweenNumbers(a, 37 , 18 , 3 )',
                            'DSL.isCardBetweenNumbers(a, 33 , 8 , 4 )',
                            'DSL.isCardBetweenNumbers(a, 3 , 31 , 1 )',
                            'DSL.isCardBetweenNumbers(a, 15 , 37 , 3 )',
                            'DSL.isBigger(a, 0 , Game.getRack() )',
                            'DSL.isBigger(a, 1 , Game.getRack() )',
                            'DSL.hasRacko(Game.getRack())',
                            'DSL.isSmaller(a, 2 , Game.getRack() )',
                            'DSL.isBigger(a, 2 , Game.getRack() )',
                            'DSL.givesRacko(a)',
                            'DSL.isCardBetweenNumbers(a, 9 , 28 , 0 )']
        self._counter_calls = []
        for i in range(len(self._strategies)):
            self._counter_calls.append(0)

    def get_counter_calls(self):
        return self._counter_calls

    def get_action(self, Game, card, hand):
        actions = Game.available_moves(card, hand)

        for a in actions:

            if DSL.isSmaller(a, 0 , Game.getRack() ):
                self._counter_calls[0] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 39 , 26 , 0 ):
                self._counter_calls[1] += 1
                return a

            if DSL.isBigger(a, 3 , Game.getRack() ):
                self._counter_calls[2] += 1
                return a

            if DSL.isSmaller(a, 4 , Game.getRack() ):
                self._counter_calls[3] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 9 , 13 , 0 ):
                self._counter_calls[4] += 1
                return a

            if DSL.isSmaller(a, 3 , Game.getRack() ):
                self._counter_calls[5] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 37 , 18 , 3 ):
                self._counter_calls[6] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 33 , 8 , 4 ):
                self._counter_calls[7] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 3 , 31 , 1 ):
                self._counter_calls[8] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 15 , 37 , 3 ):
                self._counter_calls[9] += 1
                return a

            if DSL.isBigger(a, 0 , Game.getRack() ):
                self._counter_calls[10] += 1
                return a

            if DSL.isBigger(a, 1 , Game.getRack() ):
                self._counter_calls[11] += 1
                return a

            if DSL.hasRacko(Game.getRack()):
                self._counter_calls[12] += 1
                return a

            if DSL.isSmaller(a, 2 , Game.getRack() ):
                self._counter_calls[13] += 1
                return a

            if DSL.isBigger(a, 2 , Game.getRack() ):
                self._counter_calls[14] += 1
                return a

            if DSL.givesRacko(a):
                self._counter_calls[15] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 9 , 28 , 0 ):
                self._counter_calls[16] += 1
                return a

        return actions[0]