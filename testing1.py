from simulator import T9s_89s, inEpBigCardRange, pickTwoRandomCards, inEpRange
from random import randint
from simulator2 import in25bbCallingRange
from callingHands import getCallingHands
from deck import Deck





def getRandomHandList(n):

    hand_list = []

    for i in range(n):
        lowestCards = 7
        rank = randint(lowestCards,14)
        suit = randint(0,3)
        rank2 = randint(lowestCards,14)
        suit2 = randint(0,3)
        c1 = (rank,suit)
        c2 = (rank2,suit2)
        hand_list.append((c1,c2))

    return hand_list




def testInEpRange():
    deck = Deck()

    nNotInEpRange = 0
    n = 0
    
    while (n < 500000):
        n += 1
        hand, idx1, idx2 = pickTwoRandomCards(deck)
        if (not inEpRange(hand[0], hand[1])):
            nNotInEpRange +=1

    return nNotInEpRange/n


def testin25bbCallingRange():
    for hand in getCallingHands():
        print(prettier(hand))
        print(in25bbCallingRange(hand[0], hand[1]))


def prettier(hand):
    suited = 'o'
    readableRanks = ['-','-','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    if (hand[0][1] == hand[1][1]):
        suited = 's'
    return readableRanks[hand[0][0]]+readableRanks[hand[1][0]]+suited

if __name__ == '__main__':
    # testinEpBigCardRange()

    print(1-testInEpRange())

