


"""
datana vajaita pakkoja joista poistettu EP-MP range foldeja
halutaan painoarvoja korteille: esim A: 1.1, 2: 0.9 tms

lasketaan kuinka monta mitäkin korttia on? joo?
"""

weights = []
for i in range(1,16):
    weights.append(0)

print(weights)

with open('weightedDecks.txt', 'r') as f:
    for line in f.readlines():
        it = 0
        # print(line.split(',')[:-1])
        # print(len(line.split(',')[:-1]))

        for card in line.split(',')[:-1]:
            rank = card.split(" ")[0]
            weights[int(rank)] += 1


print(weights)




