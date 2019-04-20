import simulator
from deck import Deck
from prettier import prettier

def bothCardsOver11ExclQJo(c1,c2):
    if (c1[0] >= 11 and c2[0] >= 11):
        #if QJo, return False
        if (c1[0] == 11 and c2[0] == 12 or c1[0] == 12 and c2[0] == 11):
            if (not simulator.suited(c1,c2)):
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
        if (simulator.suited(c1,c2)):
            ranks = [c1[0], c2[0]]
            if (set(ranks).isdisjoint([2,3,4])):
                return True
    return False



def in25bbCallingRange(c1,c2):

    #44+,A5s+,A7o+,KTs+,KJo+,QJs

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
    if (c1[0] == 13 and c2[0] == 10 and simulator.suited(c1,c2)):
        return True
    if (c1[0] == 10 and c2[0] == 13 and simulator.suited(c1,c2)):
        return True
    return False



#how often BB wakes up with a top17% hand 
def getCallingFreq():

    nTotal = 0
    nInRange = 0

    callingHands = []

    with open('weightedDealtHandsToBb.txt', 'r') as f:
        for line in f.readlines():
            data = line.split(" ")
            c1 = (int(data[0]), int(data[1]))
            c2 = (int(data[2]), int(data[3][:-1]))

            # print (prettier((c1,c2)))

            nTotal += 1

            if in25bbCallingRange(c1,c2):
                #OIKEE TULOS VAATIS TÄSSÄ EXAKTIN EV LASKUN; KOSKA RANGEN ERI OSIA ERI PAINOARVOILLA?
                nInRange += 1
                callingHands.append((c1,c2))

    
    print(nInRange)
    print(nTotal)
    print("freq with weights: ", nInRange/nTotal)
    print("icmizer BB calling range: ", 0.17)
    print("difference", nInRange/nTotal-0.17)
    print("how much more often v calls in percentages: ", nInRange/nTotal/0.17)


    # print(callingHands)



def tests():

    n = 0

    nTotal = 0
    nInRange = 0

    while (nTotal < 100000):
        nTotal+=1

        deck = Deck()
        hand, idx1, idx2 = simulator.pickTwoRandomCards(deck)

        if in25bbCallingRange(hand[0], hand[1]):
            #OIKEE TULOS VAATIS TÄSSÄ EXAKTIN EV LASKUN; KOSKA RANGEN ERI OSIA ERI PAINOARVOILLA?
            print(prettier(hand))
            nInRange += 1

    print(nInRange)
    print(nTotal)
    print(nInRange/nTotal)
    









if __name__ == '__main__':
    getCallingFreq()
    # tests()

    # print(inA5sPlus((14,1),(2,1)))
    # print(inA7oPlus((14,1),(2,2)))












