import random
from timeme import timeme

SHUFFLEMIN = 100
SHUFFLEVAR = 100

@timeme
def random_shuffle(listin):
    random.seed()
    shuffle_amount = random.randint(0,SHUFFLEVAR)
    listout = listin

    for i in range (0, shuffle_amount+SHUFFLEMIN):
        first = random.randint(0, len(listin)-1)
        last = random.randint(0, len(listin)-1)
        while first == last:
            last = random.randint(0, len(listin) - 1)
        temp1 = listout[first]
        listout[first] = listout[last]
        listout[last] = temp1
    return listout


print random_shuffle([1,2,3,4,5,6,7,8,9])
print random_shuffle([2,1,7,22,5,984,23,119,49,338,29,559])
