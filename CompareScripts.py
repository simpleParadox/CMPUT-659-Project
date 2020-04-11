import numpy as np
from Game import Game
from Racko import *
from copy import deepcopy
import importlib


def discard_or_deck(game):
    selection = np.random.choice(['discard', 'deck'])
    if selection == 'deck':
        return game.get_top_deck()
    return game.get_top_discard()


def get_swapped_card(old_hand, new_hand):
    # print("Old_hand",old_hand)
    # print("New hand", new_hand)
    for i in range(len(old_hand)):
        if old_hand[i] != new_hand[i]:
            return old_hand[i]


def Evaluation(player1, player2):

    victories1 = 0
    victories2 = 0
    for _ in range(100):
        # print("Game number", _ + 1)
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
                # print("player1_rack_before", game.player1_rack)
                top_card = discard_or_deck(game)
                player1_rack_copy = deepcopy(game.player1_rack)
                # print("player1_rack", game.player1_rack)
                game.player1_rack = player1.get_action(game, top_card, game.player1_rack)
                # print("Rack copy player 1", player1_rack_copy)
                # print("game rack player 1", game.player1_rack)
                if player1_rack_copy != game.player1_rack:
                    swapped_card = get_swapped_card(player1_rack_copy, game.player1_rack)
                    game.append_to_discard(swapped_card)
                else:
                    game.append_to_discard(top_card)
                current_player = 2  # Change the current player.
                game.player_turn = 2
            else:
                game.deck = game.create_new_deck()
                # print("player2_rack_before", game.player2_rack)
                top_card = discard_or_deck(game)
                player2_rack_copy = deepcopy(game.player2_rack)
                # print("player2_rack", game.player2_rack)
                game.player2_rack = player2.get_action(game, top_card, game.player2_rack)
                # print("Rack copy player 2", player2_rack_copy)
                # print("game rack player 2", game.player2_rack)
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

            # It is advisable to increase the number of moves. Initial value was 100.
            if number_of_moves >= 1000:
                is_over = True
                who_won = -1
                victories1 = -1
                victories2 = -1
                fitness1 = -1
                fitness2 = -1

                # print('No Winner!')

        if who_won == 1:
            victories1 += 1
        if who_won == 2:
            victories2 += 1
    # print(victories1, victories2)
    # print('Player 1: ', victories1 / (victories1 + victories2))
    # print('Player 2: ', victories2 / (victories1 + victories2))

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
    # score1 = 0
    # score2 = 0
    # try:
    #     score1 = victories1 / (victories1 + victories2)
    # except:
    #     score1 = -np.inf
    # try:
    #     score2 = victories2 / (victories1 + victories2)
    # except:
    #     score2 = -np.inf
    score1 = victories1 / (victories1 + victories2)
    score2 = victories2 / (victories1 + victories2)
    victories = [victories1, victories2, score1, score2]
    print("Fitness values are ", fitness)
    return victories


final_scripts_path = "C:\\Users\\Rohan\\Desktop\\Coursework\\Winter 2020\\CMPUT 659\\Projects\\Racko-Python\\"
# Instantiate scripts.
module = importlib.import_module("ScriptComb1")
class_ = getattr(module, "ScriptComb1")
script_comb_1 = class_()

module = importlib.import_module("ScriptComb2")
class_ = getattr(module, "ScriptComb2")
script_comb_2 = class_()

module = importlib.import_module("ScriptComb3")
class_ = getattr(module, "ScriptComb3")
script_comb_3 = class_()

# Instantiate OurScript
module = importlib.import_module("OurScript")
class_ = getattr(module, "OurScript")
our_script = class_()

# Comparing ScriptComb1 and OurScript
print("Comparing ScriptComb1 and OurScript")
print(Evaluation(script_comb_1, our_script))

# Comparing ScriptComb2 and OurScript
print("Comparing ScriptComb2 and OurScript")
print(Evaluation(script_comb_2, our_script))

# Comparing ScriptComb3 and OurScript
print("Comparing ScriptComb3 and OurScript")
print(Evaluation(script_comb_3, our_script))


# Switching first player turns

print("Comparing OurScript and ScriptComb1")
print(Evaluation(our_script, script_comb_1))

# Comparing ScriptComb2 and OurScript
print("Comparing OurScript and ScriptComb2")
print(Evaluation(our_script, script_comb_2))

# Comparing ScriptComb3 and OurScript
print("Comparing OurScript and ScriptComb3")
print(Evaluation(our_script, script_comb_3))