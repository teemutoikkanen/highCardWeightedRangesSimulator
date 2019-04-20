def prettier(hand):
    suited = 'o'
    readableRanks = ['-','-','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    if (hand[0][1] == hand[1][1]):
        suited = 's'
    return readableRanks[hand[0][0]]+readableRanks[hand[1][0]]+suited