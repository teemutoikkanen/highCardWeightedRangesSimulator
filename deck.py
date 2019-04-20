from random import shuffle


class Deck():

	#kortit (rank, suit), rank: 2..14, suit: 0..3 

	def __init__(self):
		self.card_list = []
		self.generate_deck()

	def generate_deck(self):
		deck = []
		for suit in range(4):
			for rank in range(2,15):
				card = (rank, suit)
				deck.append(card)
		
		shuffle(deck)
		self.card_list = deck		
		
	
			


if __name__ == "__main__":
	test = Deck()
	print(test.card_list)