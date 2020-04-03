import random
import copy


class Game():

    def __init__(self, rack):
        Game.rack = rack

    def getRack(self):

        return self.rack


    def shuffle(self, card_stack):

        random.shuffle(card_stack)


    def check_racko(self, rack):

        cards_in_order = 0
        for i in range(0, 9):
            if (rack[i] > rack[i + 1]):
                cards_in_order = cards_in_order + 1

        if cards_in_order == 9:
            return True
        else:
            return False


    def get_top_card(self, card_stack):

        return card_stack.pop()


    def deal_initial_hands(self, deck):

        computer_hand = []
        user_hand = []
        for i in range(0, 10):
        # Deal a card to the computer and remove from deck
            card_from_deck = Game.get_top_card(self, deck)
            computer_hand.append(card_from_deck)
        # Deal a card to the user and remove from deck
            card_from_deck = Game.get_top_card(self, deck)
            user_hand.append(card_from_deck)
        return (computer_hand, user_hand)


    def print_top_to_bottom(self, rack):

        for i in range(0, 10):
            print(rack[i])


    def find_and_replace(self, new_card, card_to_be_replaced, hand, discard):

        while card_to_be_replaced not in hand:
            print(hand)
            card_to_be_replaced = int(input("Please select a card in your hand to be replaced"))
        for i in range(0, 10):
            if hand[i] == card_to_be_replaced:
                open_slot = i
        hand[open_slot] = new_card
        Game.add_card_to_discard(self, card_to_be_replaced, discard)


    def add_card_to_discard(self, card, discard):

        discard.append(card)


    def computer_play(self, hand, deck, discard):

        already_replaced = []
        for x in range(0, 10):
            already_replaced.append('n')

    # Choosing whether to take card from deck or discard
        choice = Game.discard_or_deck(self, hand, discard, already_replaced)

        if choice == 'deck':
            Game.deck_strategy(self, hand, deck, discard, already_replaced)
        else:
            Game.discard_strategy(self, hand, discard, already_replaced)


    def discard_or_deck(self, hand, discard, already_replaced):

        card = discard[-1]
        if already_replaced[(40 - card) // 4] == 'n':
            return 'discard'
        else:
            return 'deck'


    def discard_strategy(self, hand, discard, already_replaced):

        card = discard.pop()
    # Divide the cards in 10 groups (1-6 is first, 7-12 is second and so on). Place the card in slot as per its group.
        card_to_be_replaced = hand[(40 - card) // 4]
        already_replaced[(40 - card) // 4] = 'y'
        hand[(40 - card) // 4] = card
        Game.add_card_to_discard(self, card_to_be_replaced, discard)


    def deck_strategy(self, hand, deck, discard, already_replaced):

        card = deck.pop()
    # Divide the cards in 10 groups (1-6 is first, 7-12 is second and so on). Place the card in slot as per its group.
        card_to_be_replaced = hand[(40 - card) // 4]
        already_replaced[(40 - card) // 4] = 'y'
        hand[(40 - card) // 4] = card
        Game.add_card_to_discard(self, card_to_be_replaced, discard)

    def available_moves(self, card, hand):

        hand1 = hand.copy
        hand2 = hand.copy
        hand3 = hand.copy
        hand4 = hand.copy
        hand5 = hand.copy

        hand1[0] = card
        hand2[1] = card
        hand3[2] = card
        hand4[3] = card
        hand5[4] = card

        moves = [hand1, hand2, hand3, hand4, hand5, hand]

        return moves






if __name__ == '__main__':
    main()