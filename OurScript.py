from Player import Player
import random
from Game import Game
from DSL import DSL


class OurScript(Player):

    def __init__(self):
        self._id = 1234567
        self._strategies = ['DSL.isCardBetweenNumbers( a, 1 , 8 , 0) ',
                            'DSL.isCardBetweenNumbers( a, 9 , 16 , 1 ) ',
                            'DSL.isCardBetweenNumbers( a, 17 , 25 , 2 ) ',
                            'DSL.isCardBetweenNumbers( a, 26 , 34 , 3 ) ',
                            'DSL.isCardBetweenNumbers( a, 35 , 40 , 4 ) ']
        self._counter_calls = []
        for i in range(5):
            self._counter_calls.append(0)

    def get_counter_calls(self):
        return self._counter_calls

    def get_action(self, Game, card, hand):
        actions = Game.available_moves(card, hand)

        for a in actions:

            if DSL.isCardBetweenNumbers( a, 1 , 8 , 0):
                self._counter_calls[0] += 1
                return a

            if DSL.isCardBetweenNumbers( a, 9 , 16 , 1 ):
                self._counter_calls[1] += 1
                return a

            if DSL.isCardBetweenNumbers( a, 17 , 25 , 2 ):
                self._counter_calls[2] += 1
                return a

            if DSL.isCardBetweenNumbers( a, 26 , 34 , 3 ):
                self._counter_calls[3] += 1
                return a

            if DSL.isCardBetweenNumbers( a, 35 , 40 , 4 ):
                self._counter_calls[4] += 1
                return a

        return actions[0]