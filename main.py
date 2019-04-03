from deck import Deck
from random import randint
#test0: 8 handed, folded to SB, get weighted values for rest of the deck
#siis.. forceen bottom range kädet jaettavaks
#tallenan loppupakan

rfiRanges = []


def test0():

	deck = Deck()

	tableSize = 8
	
	# number of folded combinations before the small bind
	nFolds = tableSize-2


	# force bottom-range deal for each range

	for i in range(nFolds):

		#generate two unique ints to randomly pick cards
		randint1 = randint(0,len(deck.cardList)-1)
		randint2 = randint(0,len(deck.cardList)-1)
		while (randint2 ==  randint1):
			randint2 = randint(0,len(deck.cardList)-1)

		c1 = deck.cardList[randint(0,len(deck.cardList)-1)]
		c2 = deck.cardList[randint(0,len(deck.cardList)-1)]

		hand = (c1, c2)


		#i 0-2 EP, 3-6 CO, 7 BTN

		if (i < 3):
			#force ep folding range deal, remove cards from deck
			
		elif (i < 7):
			#force mp folding range deal, remove from deck
		else:
			#force btn folding rande deal, remove from deck
		

	#now we have remaining deck, append it to a file 


	# ... do analysis later


	




