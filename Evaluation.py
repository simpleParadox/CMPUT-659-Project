import random
import numpy as np
import random
import collections
from game import Board, Game
from players.scripts.player_test import PlayerTest
from players.scripts.player_random import PlayerRandom
from players.scripts.DSL import DSL
import sys
from players.scripts.Script import Script
import importlib
# module = importlib.import_module("Users.casspirlot.PycharmProjects.CANTSTOP.players.Generated.Script" + str(list1[0].getId()))
# class_ = getattr(module, "Script" + str(list1[0].getId()))
# instance_script1 = class_()

def initializePopulation(size, generation, depth):
    list1 = []
    for i in range(size):
        choose = random.randint(1, 5)
        Try = DSL()
        OK = Script(Try.initializeNumerous(choose, depth),  i)
        list1.append(OK)
        OK.saveFile("/Users/casspirlot/PycharmProjects/CANTSTOP/players/Generated/")

    return list1


def Evaluation(player1, player2):

    victories1 = 0
    victories2 = 0
    for _ in range(100):
        game = Game(n_players=2, dice_number=4, dice_value=3, column_range=[2, 6],
                    offset=2, initial_height=1)

        is_over = False
        who_won = None

        number_of_moves = 0
        current_player = game.player_turn
        while not is_over:
            moves = game.available_moves()
            if game.is_player_busted(moves):
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
                continue
            else:
                if game.player_turn == 1:
                    chosen_play = player1.get_action(game)
                else:
                    chosen_play = player2.get_action(game)
                if chosen_play == 'n':
                    if current_player == 1:
                        current_player = 2
                    else:
                        current_player = 1
                print('Chose: ', chosen_play)
                # game.print_board()
                game.play(chosen_play)
                game.print_board()
                number_of_moves += 1

                print()
            who_won, is_over = game.is_finished()

            if number_of_moves >= 200:
                is_over = True
                who_won = -1
                victories1 = -1
                victories2 = -1
                fitness1 = -1
                fitness2 = -1

                print('No Winner!')

        if who_won == 1:
            victories1 += 1
        if who_won == 2:
            victories2 += 1
    print(victories1, victories2)
    print('Player 1: ', victories1 / (victories1 + victories2))
    print('Player 2: ', victories2 / (victories1 + victories2))

    if victories1 > victories2:
            fitness1 = 1
            fitness2 = -1

    if victories1 < victories2:
        fitness1 = -1
        fitness2 = 1

    if victories1 == victories2:
        fitness1 = -1
        fitness2 = -1

    fitness = [fitness1, fitness2]
    victories = [victories1, victories2, victories1 / (victories1 + victories2), victories2 / (victories1 + victories2)]
    return victories



def Eval(dictionary,times):
    for i in dictionary.keys():
        for j in dictionary.keys():
            if i != j:
                for k in range(times):
                    Play = Evaluation(i,j)

def Eval(dictionary,times):
    for i in dictionary.keys():
        for j in dictionary.keys():
            if i != j:
                for k in range(times):
                    Play = Evaluation(i,j)
                    dictionary[i] += Play[0]
                    dictionary[j] += Play[1]
    return dictionary




# from players.scripts.PotWinner2 import Script2539
#
# ok = Script2539()
#
# from players.scripts.FirstForOne import Script189
#
# okk = Script189()
# dict = {ok:0, okk:0}
#
# print(Eval(dict,40))

def Elite(dictionary, num):

    eliteDict = {}
    for i in dictionary.keys():
        eliteDict[i] = dictionary[i]
    while len(eliteDict) > num:
        del eliteDict[min(eliteDict, key=lambda k: eliteDict[k])]

    return eliteDict




def Tournament(t, dictionary):
    list = []
    for key in dictionary.keys():
        list.append(key)
    tournDict = {}
    for i in range(t):
        j = random.randint(0, len(list)-1)
        tournDict[list[j]] = dictionary[list[j]]
        list.remove(list[j])

    return max(tournDict, key=lambda k: tournDict[k])



def generateSplit(parent1, parent2):

    split_index1 = random.randint(0, len(parent1._strategies))
    print(split_index1)
    parent1_1 = parent1._strategies[0:split_index1+1]
    parent1_2 = parent1._strategies[split_index1 + 1: len(parent1._strategies)]
    print("parent 1 split")

    print(parent1_1)
    print(parent1_2)


    split_index2 = random.randint(0, len(parent2._strategies))

    print(split_index2)
    parent2_1= parent2._strategies[0:split_index2]
    parent2_2 = parent2._strategies[split_index2: len(parent2._strategies)]
    print("parent 2 split")

    print(parent2_1)
    print(parent2_2)

    choose = random.randint(0,3)
    print('choose')
    print(choose)
    if choose == 0:
        childStrat = np.concatenate([parent1_1, parent2_1])
    if choose == 1:
        childStrat = np.concatenate([parent1_1, parent2_2])
    if choose == 2:
        childStrat = np.concatenate([parent1_2, parent2_1])
    if choose == 3:
        childStrat = np.concatenate([parent1_2, parent2_2])

    if len(childStrat)==0:
        childStrat = np.array(parent1._strategies)

    return childStrat.tolist()


def crossover(parent1, parent2,i):
    childStrat = generateSplit(parent1, parent2)
    Ok = Script(childStrat, i)
    Ok.saveFile("/Users/casspirlot/PycharmProjects/CANTSTOP/players/Generated/")
    return Ok



def mutate(script, j):
    Try = DSL()
    new = []

    for i in range(len(script._strategies)):
        if random.randint(0,1)==0:
            new.append(Try.initialize('S',3))
        if random.randint(0,1)==0:
            new.append(Try.initialize('S',3))
        else:
            new.append(script._strategies[i])
        if random.randint(0, 1) == 0:
            new.append(Try.initialize('S',3))
            print('p')
        print(new)

    Ok = Script(new, script._id + j)
    Ok.saveFile("/Users/casspirlot/PycharmProjects/CANTSTOP/players/Generated/")
    return Ok



def RemoveUnused(dictionary,indictator):
    newDict = {}
    ListoKeys = []
    for guy in dictionary.keys():
        ListoKeys.append(guy)
        print(ListoKeys)

    for h in ListoKeys:
        fitVal = dictionary[h]
        print("line 203")
        print(fitVal)

        deleteList = []
        for i in range(len(h._strategies)):
            if h._counter_calls[i] == 0:
                deleteList.append(h._strategies[i])
            print("210")
            print(deleteList)
        for bad in deleteList:
            print('213')
            print(h._strategies)
            h._strategies.remove(bad)
            print(h._strategies)


        if len(h._strategies) != 0:

            Ok = Script(h._strategies, h._id + indictator+70)
            Ok.saveFile("/Users/casspirlot/PycharmProjects/CANTSTOP/players/Generated/")
            module = importlib.import_module("players.Generated.Script" + str(Ok.getId()))
            class_ = getattr(module, "Script" + str(Ok.getId()))
            inst = class_()
            newDict[inst] = fitVal
            print("IN IF")
            print(fitVal)
            print(newDict)
            print(inst)

        else:
            Try = DSL()
            OK = Script(Try.initializeNumerous(3, 3), h._id +70 + indictator)
            OK.saveFile("/Users/casspirlot/PycharmProjects/CANTSTOP/players/Generated/")
            module = importlib.import_module("players.Generated.Script" + str(OK.getId()))
            class_ = getattr(module, "Script" + str(OK.getId()))
            inst = class_()
            newDict[inst] = 0
            print("IN ELSE")

    return newDict


def EZS(generationNum, populationNum, eliteNum, tournamentNum, mutationNum):
    indexPop = 0
    list1 = initializePopulation(populationNum, 1, 3)
    print("Line 245: ")
    print(list1)
    instList1 = []
    for k in range(len(list1)):
        module = importlib.import_module("players.Generated.Script" + str(list1[k].getId()))
        class_ = getattr(module, "Script" + str(list1[k].getId()))
        inst = class_()
        instList1.append(inst)
    print("Line 253: ")
    print(instList1)

    Dictionary = {}
    for guy in instList1:
        Dictionary[guy] = 0
    print("line 259")
    print(Dictionary)

    for l in range(generationNum):
        indexPop +=1
        for key in Dictionary.keys():
            Dictionary[key] = 0
            print("line 310")
            print(Dictionary)

        Dictionary2 = Eval(Dictionary, 1)
        print(Dictionary2)

        Dictionary2 = RemoveUnused(Dictionary2, indexPop*100)
        print(Dictionary2)

        P_prime = {}
        elite = Elite(Dictionary2, eliteNum)
        print(Dictionary)
        print("line 270")
        print(elite)

        P_prime.update(elite)
        print('line 274')
        print(P_prime)

        numberIt = 0
        while len(P_prime) < len(Dictionary2):
            p_1 = Tournament(tournamentNum, Dictionary2)
            p_2 = Tournament(tournamentNum, Dictionary2)
            c = crossover(p_1, p_2, indexPop*100 + 99)

            module = importlib.import_module("players.Generated.Script" + str(c.getId()))
            class_ = getattr(module, "Script" + str(c.getId()))
            inst = class_()

            newC = mutate(inst, indexPop*100)
            module = importlib.import_module("players.Generated.Script" + str(newC.getId()))
            class_ = getattr(module, "Script" + str(newC.getId()))
            inst = class_()

            P_prime[inst] = 0
            numberIt += 1

        print('line 299')
        print(P_prime)

        Dictionary = P_prime

    Dictionary2 = Eval(Dictionary,3)
    print('line 305')
    print(Dictionary2)

    print(Elite(Dictionary2,1))

    return Dictionary2




print(EZS(1,3,1,2,1))