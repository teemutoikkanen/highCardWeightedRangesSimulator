from random import shuffle


class Deck():

	#kortit (rank, suit), rank: 2..14, suit: 0..3 

	def __init__(self):
		self.cardList = []
		self.generateDeck()

	def generateDeck(self):
		deck = []
		for suit in range(4):
			for rank in range(2,15):
				card = (rank, suit)
				deck.append(card)
		
		shuffle(deck)
		self.cardList = deck		
		
	
			


if __name__ == "__main__":
	test = Deck()
	print(test.cardList)