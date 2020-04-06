# Program to make a game of Racko (Computer versus 1 Player)
import random

def print_intro():
	'''
	Introduce the user to the game and rules
	'''
	print('''Welcome to Racko!	
	You will be dealt 10 cards (Your Rack) out of a Racko deck, which is composed of 40 cards, each numbered 1 to 40.
	The objective is to be the first player to arrange all of the cards in your rack from highest to lowest (Top to Bottom).
	The top card of the deck is turned over to start the discard pile. Each turn, you can take the top card from either the deck or the discard pile, then discard one from your rack and insert the new card in its place. 
	If you draw a card from the deck, you may immediately discard it; if you take the top discard, though, you must put it into your rack.
	Note that when the cards are dealt, it gets placed in the hand from back to front.
	''')
def main():
	'''
	Main function which defines game elements and game flow
	'''
	#Introduce the game rules
	print_intro()

	#Define the Racko deck and the discard pile
	deck = []
	for card in range(1,41):
		deck.append(card)
	discard = []
	shuffle(deck)
	
	#Deal hands to both user and computer
	hands = deal_initial_hands(deck)
	computer_hand = hands[0]
	user_hand = hands[1]

	#Start the discard pile by turning over the top card from the deck
	add_card_to_discard(get_top_card(deck),discard)

	print("Your current hand is:")
	print_top_to_bottom(user_hand)

	racko_flag = 0

	while racko_flag is not True:
		#User plays first. Show him the discard pile top card.
		print("The current card in discard pile is:", discard[-1])
		choice = input("Do you want to take this card? y/n")
		#If user wants the discard pile card, ask him to replace one of his hand cards
		if choice == 'y':
			card = discard.pop()
			card_to_be_replaced = input("Which card do you want to replace?")
			find_and_replace(card,card_to_be_replaced,user_hand,discard)
		#If user does not want the discard pile card, show him the deck card
		elif choice == 'n':
			card = deck.pop()
			print("The top card in the deck is:", card)
			second_choice = input("Do you want to take this card? y/n")
			#If user wants the deck card, ask him to replace one of his hand cards
			if second_choice == 'y':
				card_to_be_replaced = input("Which card do you want to replace?")
				find_and_replace(card,card_to_be_replaced,user_hand,discard)
			#If user does not want the deck card, add it to the discard pile
			else:
				discard.append(card) # Pass my turn
		print("Your current hand is:")
		print_top_to_bottom(user_hand)

		# Determine what move the computer will make
		computer_play(computer_hand,deck,discard)

		#Check whether Racko has been achieved
		racko_flag = check_racko(user_hand) or check_racko(computer_hand)

		#Check if there are cards left in the deck. if not, shuffle the discard pile and make a new deck.
		if len(deck) < 1:
			shuffle(discard)
			deck.extend(discard)
			discard = []
			add_card_to_discard(get_top_card(deck),discard)
		else:
			continue

	if check_racko(user_hand) == 1:
		print("Congrats! You win. Computer's hand:")
		print_top_to_bottom(computer_hand)
	elif check_racko(computer_hand) == 1:
		print("You lose. Better luck next time. Computer's hand:")
		print_top_to_bottom(computer_hand)
	else:
		print("Error. No racko.")


def shuffle(card_stack):
	'''
	Shuffles a deck (List) of cards
	'''
	random.shuffle(card_stack)

def check_racko(rack):
	'''
	Checks if a rack (Player's hand) is arranged in an ascending order - Condition for winning the game
	'''
	cards_in_order = 0
	for i in range(0,5):
		if (rack[i] > rack[i+1]):
			cards_in_order = cards_in_order + 1
	#print cards_in_order
	if cards_in_order == 5:
			return True
	else:
		return False

def get_top_card(card_stack):
	'''
	Draws the top card from a given deck
	'''
	return card_stack.pop()

def deal_initial_hands(deck):
	'''
	Deals 10 cards to both computer and player. The cards are arranged in racks as per Racko rules.
	'''
	computer_hand = []
	user_hand = []
	for i in range(0,10):
		#Deal a card to the computer and remove from deck
		card_from_deck = get_top_card(deck)
		computer_hand.append(card_from_deck)
		#Deal a card to the user and remove from deck
		card_from_deck = get_top_card(deck)
		user_hand.append(card_from_deck)
	return(computer_hand,user_hand)

def print_top_to_bottom(rack):
	'''
	Prints a given list in a vertical format
	'''
	for i in range(0,10):
		print (rack[i])

def find_and_replace(new_card,card_to_be_replaced,hand,discard):
	'''
	Swaps in a new card into a rack, and adds the replaced card to the discard pile
	'''
	while card_to_be_replaced not in hand:
		print(hand)
		card_to_be_replaced = int(input("Please select a card in your hand to be replaced"))
	for i in range(0,10):
		if hand[i] == card_to_be_replaced:
			open_slot = i
	hand[open_slot] = new_card
	add_card_to_discard(card_to_be_replaced,discard)
	

def add_card_to_discard(card,discard):
	'''
	Adds a card to the discard pile
	'''
	discard.append(card)

def computer_play(hand,deck,discard):
	'''
	Defines computer's strategy given a hand and the top card of the deck and discard piles
	'''
	already_replaced = []
	for x in range(0,10):
		already_replaced.append('n')

	#Choosing whether to take card from deck or discard
	choice = discard_or_deck(hand,discard,already_replaced)	

	if choice == 'deck':
		deck_strategy(hand,deck,discard,already_replaced)
	else:
		discard_strategy(hand,discard,already_replaced)


def discard_or_deck(hand,discard,already_replaced):
	'''
	Makes the choice whether the computer should pick a card from discard or deck.
	'''
	#Take the discard card, unless the card in the slot has already been replaced previously
	card = discard[-1]
	if already_replaced[(40-card)//4] == 'n':
		return 'discard'
	else:
		return 'deck'

def discard_strategy(hand,discard,already_replaced):
	'''
	Determines computer's play in case it picks up a discard pile card
	'''
	card = discard.pop()
	#Divide the cards in 10 groups (1-6 is first, 7-12 is second and so on). Place the card in slot as per its group.
	card_to_be_replaced = hand[(40-card) // 4]
	already_replaced[(40-card)//4] = 'y'
	hand[(40-card) // 4] = card
	add_card_to_discard(card_to_be_replaced,discard)

def deck_strategy(hand,deck,discard,already_replaced):
	'''
	Determines computer's play in case it picks up a discard pile card
	'''
	card = deck.pop()
	#Divide the cards in 10 groups (1-6 is first, 7-12 is second and so on). Place the card in slot as per its group.
	card_to_be_replaced = hand[(40-card) // 4]
	already_replaced[(40-card)//4] = 'y'
	hand[(40-card) // 4] = card
	add_card_to_discard(card_to_be_replaced,discard)



if __name__ == '__main__':
	main()