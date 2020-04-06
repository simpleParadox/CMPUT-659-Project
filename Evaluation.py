import random
import numpy as np
import random
import collections
from Game import Game
from DSL import DSL
import sys
from Player import Player
from Racko import *
from Script import Script
from copy import deepcopy

import importlib
# module = importlib.import_module("Users.casspirlot.PycharmProjects.CANTSTOP.players.Generated.Script" + str(list1[0].getId()))
# class_ = getattr(module, "Script" + str(list1[0].getId()))
# instance_script1 = class_()
path = "C:\\Users\\Rohan\\Desktop\\Coursework\\Winter 2020\\CMPUT 659\\Projects\\Racko-Python\\Population\\"
def initializePopulation(size, generation, depth):
    list1 = []
    # The following line is the directory on Rohan's computer, change
    # this to the directory where you would like to store your scripts.

    for i in range(size):
        choose = random.randint(1, 5)
        Try = DSL()
        OK = Script(Try.initializeNumerous(choose, depth),  i)
        list1.append(OK)
        OK.saveFile(path)

    return list1


def discard_or_deck(game):
    selection = np.random.choice(['discard', 'deck'])
    if selection == 'deck':
        return game.get_top_deck()
    return game.get_top_discard()

def get_swapped_card(old_hand, new_hand):
    print("Old_hand",old_hand)
    print("New hand", new_hand)
    for i in range(len(old_hand)):
        if old_hand[i] != new_hand[i]:
            return old_hand[i]



def Evaluation(player1, player2):

    victories1 = 0
    victories2 = 0
    for _ in range(1):
        game = Game()

        who_won = None

        number_of_moves = 0
        current_player = game.player_turn
        is_over = False
        while not is_over:
            # moves = game.available_moves()
            game.deck = game.create_new_deck()
            if current_player == 1:
                # Get the card from either the top deck or the discard pile.
                # Choose whether to take card from discard or rack'o deck.
                game.deck = game.create_new_deck()
                print("player1_rack_before", game.player1_rack)
                top_card = discard_or_deck(game)
                player1_rack_copy = deepcopy(game.player1_rack)
                print("player1_rack", game.player1_rack)
                game.player1_rack = player1.get_action(game, top_card, game.player1_rack)
                print("Rack copy player 1", player1_rack_copy)
                print("game rack player 1", game.player1_rack)
                if player1_rack_copy != game.player1_rack:
                    print("hello world")
                    swapped_card = get_swapped_card(player1_rack_copy, game.player1_rack)
                    game.append_to_discard(swapped_card)
                else:
                    game.append_to_discard(top_card)
                current_player = 2  # Change the current player.
                game.player_turn = 2
            else:
                game.deck = game.create_new_deck()
                print("player2_rack_before", game.player2_rack)
                top_card = discard_or_deck(game)
                player2_rack_copy = deepcopy(game.player2_rack)
                print("player2_rack", game.player2_rack)
                game.player2_rack = player2.get_action(game, top_card, game.player2_rack)
                print("Rack copy player 2", player2_rack_copy)
                print("game rack player 2", game.player2_rack)
                if player2_rack_copy != game.player2_rack:
                    swapped_card = get_swapped_card(player2_rack_copy, game.player2_rack)
                    game.append_to_discard(swapped_card)
                else:
                    game.append_to_discard(top_card)
                current_player = 1
                game.player_turn = 1


            # if chosen_play == 'n':
            #     if current_player == 1:
            #         current_player = 2
            #     else:
            #         current_player = 1
            # print('Chose: ', chosen_play)
            # # game.print_board()
            # game.play(chosen_play)
            # game.print_board()
            number_of_moves += 1
            if game.check_racko(game.player1_rack) is True:
                who_won = 1
                is_over = True
            if game.check_racko(game.player2_rack) is True:
                who_won = 2
                is_over = True

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
    print("Fitness values are ", fitness)
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
    Ok.saveFile(path)
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
    Ok.saveFile(path)
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
            Ok.saveFile(path)
            module = importlib.import_module("Population.Script" + str(Ok.getId()))
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
            OK.saveFile(path)
            module = importlib.import_module("Population.Script" + str(OK.getId()))
            class_ = getattr(module, "Script" + str(OK.getId()))
            inst = class_()
            newDict[inst] = 0
            print("IN ELSE")

    return newDict


def EZS(generationNum, populationNum, eliteNum, tournamentNum):
    indexPop = 0
    list1 = initializePopulation(populationNum, 1, 3)
    print("Line 245: ")
    print(list1)
    instList1 = []
    for k in range(len(list1)):
        module = importlib.import_module("Population.Script" + str(list1[k].getId()))
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

            module = importlib.import_module("Population.Script" + str(c.getId()))
            class_ = getattr(module, "Script" + str(c.getId()))
            inst = class_()

            newC = mutate(inst, indexPop*100)
            module = importlib.import_module("Population.Script" + str(newC.getId()))
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

    return Elite(Dictionary2,1)




d = EZS(generationNum=1,populationNum=3,eliteNum=1,tournamentNum=2)
for key in d.keys():
    print(key._strategies)

# add_swapped_card_to_discard([1,2,3,4],[9,2,3,4])