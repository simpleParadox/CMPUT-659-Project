from Player import Player
import random
from Game import Game
from DSL import DSL


class ScriptComb1(Player):

    def __init__(self):
        self._id = 1001
        self._strategies = ['DSL.isBigger(a, 2 , Game.getRack() )',
                            'DSL.givesRacko(a)', 'DSL.hasRacko(Game.getRack())',
                            'DSL.isCardBetweenNumbers(a, 21 , 12 , 3 )',
                            'DSL.isCardBetweenNumbers(a, 26 , 33 , 3 )',
                            'DSL.isCardBetweenNumbers(a, 4 , 34 , 4 )',
                            'DSL.isBigger(a, 1 , Game.getRack() )',
                            'DSL.isSmaller(a, 3 , Game.getRack() )',
                            'DSL.isCardBetweenNumbers(a, 12 , 3 , 2 )']
        self._counter_calls = []
        for i in range(len(self._strategies)):
            self._counter_calls.append(0)

    def get_counter_calls(self):
        return self._counter_calls

    def get_action(self, Game, card, hand):
        actions = Game.available_moves(card, hand)

        for a in actions:

            if DSL.isBigger(a, 2 , Game.getRack() ):
                self._counter_calls[0] += 1
                return a

            if DSL.givesRacko(a):
                self._counter_calls[1] += 1
                return a

            if DSL.hasRacko(Game.getRack()):
                self._counter_calls[2] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 21 , 12 , 3 ):
                self._counter_calls[3] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 26 , 33 , 3 ):
                self._counter_calls[4] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 4 , 34 , 4 ):
                self._counter_calls[5] += 1
                return a

            if DSL.isBigger(a, 1 , Game.getRack() ):
                self._counter_calls[6] += 1
                return a

            if DSL.isSmaller(a, 3 , Game.getRack() ):
                self._counter_calls[7] += 1
                return a

            if DSL.isCardBetweenNumbers(a, 12 , 3 , 2 ):
                self._counter_calls[8] += 1
                return a
        return actions[0]