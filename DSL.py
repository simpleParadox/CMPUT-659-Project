import copy
import random
from Script import Script
from Game import Game
path = "C:\\Users\\Rohan\\Desktop\\Coursework\\Winter 2020\\CMPUT 659\\Projects\\Racko-Python\\Population\\"
class DSL:

    def __init__(self):

        self.start = 'S'

        self._grammar = {}
        self._grammar[self.start] = ['if B S', '']
        self._grammar['B'] = ['B1', 'B1 and B1']
        self._grammar['B1'] = ['DSL.isBigger(a, INDEX , Game.getRack() ) ',
                               'DSL.isSmaller(a, INDEX , Game.getRack() )', 'DSL.givesRacko(a)',
                               'DSL.hasRacko(Game.getRack())',
                               'DSL.isCardBetweenNumbers(a, NUMBER , NUMBER , INDEX , Game.getRack() )']
        self._grammar['INDEX'] = ['0', '1', '2', '3', '4']
        self._grammar['NUMBER'] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                   '11', '12', '13', '14', '15', '16', '17', '18',
                                   '19', '20', '21', '22', '23', '24', '25', '26', '27',
                                   '28','29', '30', '31', '32', '33', '34', '35', '36',
                                   '37', '38', '39']



    @staticmethod
    def isBigger(action, index, hand):
        """
        Returns True if the card selected is larger than the index
        :param action: Card picked up
        :param index: place in players rack
        :return: T/F
        """

        # I think this function needs to be more clear and redefined.
        # I do understand what you are trying to do but I believe the variables are inconsistent.
        # print("Action is ", action)
        if index > 0 and action[index] > hand[index-1]:
            return True
        else:
            return False

    @staticmethod
    def isSmaller(action, index, hand):
        """
        Returns True if the card selected is larger than the index

        """

        if index < 4 and action[index] < hand[index + 1]:
            return True
        else:
            return False

    @staticmethod
    def givesRacko(action):
        """
        Returns true if action will result in Racko

        """
        # print(action)
        if action[0] < action[1] < action[2] < action[3] < action[4]:
            return True
        else:
            return False

    @staticmethod
    def hasRacko(hand):
        """
        Returns true if the hand has racko

        """
        if hand[0] < hand[1] < hand[2] < hand[3] < hand[4]:
            return True
        else:
            return False

    # @staticmethod
    # def isCardNumber(action, number):
    #     # Checks whether the picked up card from any of the decks is a certain number.
    #     if action == number:
    #         return True
    #     return False

    @staticmethod
    def isCardBetweenNumbers(action, number1, number2, index, hand):
        # Generic function to check whether the picked up card is between two numbers.
        for i in range(5):
            if action[i] == hand[i]:
                pass
            else:
                new = i
                if number1 <= number2 and new == index:
                    if number1 <= action[new] <= number2:
                        return True
                    return False
                elif new == index:
                    if number2 <= action[new] <= number1:
                        return True
                    return False

    ####################################################

    def initialize(self, symbol, depth, counter = 0):

        if depth == 0:
            pass

        if symbol not in self._grammar:
            # print('terminated')
            return symbol + ' '

        string = ''
        if counter == 0 and symbol == 'S':
            expression_list = self._grammar[symbol][0].split(' ')
            # print('in if')
            # print(expression_list)
            for symb in expression_list:
                string = string + str(self.initialize(symb, depth-1, counter+1))

        else:
            if symbol == 'S':
                pass
            else:
                index = random.randint(0, len(self._grammar[symbol])-1)
                # print(index)
                # print(symbol)
                expressionList = self._grammar[symbol][index].split(' ')
                # print('in else')
                # print(expressionList)
                for symb in expressionList:
                    string = string + str(self.initialize(symb, depth - 1, counter + 1))
        return string


    def initializeNumerous(self, number, depth):
        Array = []
        for i in range(number):
           Array.append(self.initialize('S',depth))

        return Array

    def initializePopulation(self, size, depth):
        list1 = []
        for i in range(size):
            choose = random.randint(1, 5)
            Try = DSL()
            OK = Script(Try.initializeNumerous(choose, depth), i)
            list1.append(OK)
            OK.saveFile(path)

        return list1
 ###########################



Try = DSL()

print(Try.initializeNumerous( 3, 3))

Try.initializePopulation(3,3)