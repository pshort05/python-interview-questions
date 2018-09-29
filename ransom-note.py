"""""
Sample Input:
7 5
two two three is not four four
two times two is four
Sample Output:
Yes
"""""
import itertools

def ransom_note(magazine, ransom):
    mags = {}

    for m in magazine:
        if mags.has_key(m):
            mags[m] += 1
        else:
            mags[m] = 1

    for m in ransom:
        if mags.has_key(m) and mags[m] > 0:
            mags[m] -= 1
        else:
            return False
    return True


m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print "Yes"
else:
    print "No"

