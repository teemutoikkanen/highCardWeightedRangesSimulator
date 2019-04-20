from deck import Deck
from random import randint
import time
from prettier import prettier
# test0: 8 handed, folded to SB, get weighted values for rest of the deck
# siis.. forceen bottom range kädet jaettavaks
# tallenan loppupakan

def bothCardsOver11ExclQJo(c1,c2):
    if (c1[0] >= 11 and c2[0] >= 11):
        #if QJo, return False
        if (c1[0] == 11 and c2[0] == 12 or c1[0] == 12 and c2[0] == 11):
            if (not suited(c1,c2)):
                return False
        return True
    return False

def inA7oPlus(c1,c2):
    if (c1[0] == 14 or c2[0] == 14):
        ranks = [c1[0], c2[0]]
        if (set(ranks).isdisjoint([2,3,4,5,6])):
            return True
    return False

def inA5sPlus(c1,c2):
    if (c1[0] == 14 or c2[0] == 14):
        if (suited(c1,c2)):
            ranks = [c1[0], c2[0]]
            if (set(ranks).isdisjoint([2,3,4])):
                return True
    return False



def in25bbCallingRange(c1,c2):

    # VANHA VÄÄRÄ -------------44+,A5s+,A7o+,KTs+,KJo+,QJs
    


    # 33+,A2s+,A3o+,K8s+,K9o+,QTs+,QJo,JTs 
    # TODO !

    
    #i.e. 
    #   both cards over 11, excluding QJo,
    if (bothCardsOver11ExclQJo(c1,c2)):
        return True
    #   44+
    if (c1[0] == c2[0] and c1[0] >= 4):
        return True
    #   A7o+
    if (inA7oPlus(c1,c2)):
        return True
    #   A5s+
    if (inA5sPlus(c1,c2)):
        return True
    #   KTs
    if (c1[0] == 13 and c2[0] == 10 and suited(c1,c2)):
        return True
    if (c1[0] == 10 and c2[0] == 13 and suited(c1,c2)):
        return True
    return False

def T9s_89s(c1, c2):
    if (c1[1] == c2[1]):
        if (c1[0] == 9 or c2[0] == 9):
            if (c1[0] == 10 or c2[0] == 10):
                return True
            if (c1[0] == 8 or c2[0] == 8):
                return True
    return False


def suited(c1, c2):
    if (c1[1] == c2[1]):
        return True
    return False


def suitedAce(c1, c2):
    if (suited(c1, c2)):
        if (c1[0] == 14 or c2[0] == 14):
            return True
    return False


def inEpBigCardRange(c1, c2):
    if (c1[0] >= 10 and c2[0] >= 10):
        # if exactly one T
        if (c1[0] == 10 or c2[0] == 10 and c1[0] != c2[0]):
            # if not suited
            if (not suited(c1,c2)):
                # if other card is K, Q or J, return False
                ranks = [c1[0], c2[0]]
                if (11 in ranks or 12 in ranks):
                    return False
        return True
    return False


# return true if hand in EP/TOP18% rannge
def inEpRange(c1, c2):

    # if pair >= 33
    if (c1[0] == c2[0] and c1[0] != 2):
        return True

    # if both cards are above T, excluding KTo,QTo,JTo
    if (inEpBigCardRange(c1,c2)):
        return True

    # if T9s,89s
    if (T9s_89s(c1, c2)):
        return True

    # if A*:ss
    if (suitedAce(c1,c2)):
        return True
    return False


def pickTwoRandomCards(deck):
    # generate two unique ints to randomly pick cards
    randint1 = randint(0,len(deck.card_list)-1)
    randint2 = randint(0,len(deck.card_list)-1)
    while (randint2 == randint1):
        randint2 = randint(0,len(deck.card_list)-1)

    c1 = deck.card_list[randint1]
    c2 = deck.card_list[randint2]

    return (c1, c2), randint1, randint2

def foldedToSbSim():

    deck = Deck()

    #remove SB hole cards (Q9o)
    deck.card_list.remove((12,0))
    deck.card_list.remove((9,1))

    tableSize = 8
    
    # number of folded combinations before the small bind
    nFolds = tableSize-2


    # force bottom-range deal for each range

    for i in range(nFolds):

        while (True):
            hand, idx1, idx2 = pickTwoRandomCards(deck)

            if (not inEpRange(hand[0], hand[1])):
                #remove cards from deck (higher first so it doesnt mess up the lower numbers)
                if (idx1 > idx2):
                    del deck.card_list[idx1]
                    del deck.card_list[idx2]
                else:
                    del deck.card_list[idx2]
                    del deck.card_list[idx1]
                break


    #with the remaining deck, force Q9o to hero (DONE, BEFORE RANDOM CARD DEALS, LINE 84)

    #deal random hand to BB until its a 17% calling-range hand, save frequencies
    nTotal = 0
    nCallingHand = 0

    while (True):
        nTotal += 1
        hand,idx1,idx2 = pickTwoRandomCards(deck)


        if (in25bbCallingRange(hand[0], hand[1])):
            nCallingHand += 1
            break


    return nTotal, nCallingHand


            
    # # now we have remaining deck, append it to a file
    # with open('weightedDecks.txt', 'a') as f:
    #     for card in deck.card_list:
    #         f.write(str(card[0]) + " " + str(card[1]) + ",")
    #     f.write("\n")
    # # ... do analysis later
    

    #with the remaining deck, deal a random combination, save that to a file, analyze later

    # with open('weightedDealtHandsToBb.txt', 'a') as f:
    #     hand, idx1, idx2 = pickTwoRandomCards(deck)
    #     c1r = hand[0][0]
    #     c1s = hand[0][1]
    #     c2r = hand[1][0]
    #     c2s = hand[1][1]
    #     f.write(str(c1r) + " " + str(c1s) + " " + str(c2r) + " " + str(c2s) + "\n")

    



    
if __name__ == '__main__':
    print(time.time())
    n = 10**6

    deals = 0
    wakeups = 0

    for i in range(n):
        nTotal, nWakeups = foldedToSbSim()

        deals += nTotal
        wakeups += nWakeups

        if (i % 5000 == 0):
            print("i: ",i)
            print(time.time())
            # print(sum(1 for line in open('weightedDealtHandsToBb.txt')))
            print("deals, wakeups: ", deals, wakeups)
            print("wakeup frequency: ", wakeups/deals)

            # wakeup frequency:  0.18253405316824406


    # print(nIterations)
    # print(nInEpRange)