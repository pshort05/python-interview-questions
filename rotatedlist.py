""""
Given a sorted array rotated at an unknown point, write a function that locates that point.

Input: [5, 6, 1, 2, 3, 4]
Output: 2
"""

def find_inflection(slist):

    min = slist[0]
    max = slist[0]

    for x in range (0, len(slist)):
        if slist[x] < min:
            # found inflection point
            return x
        if slist[x] > max:
            max = slist[x]
    return 0


print find_inflection([5, 1, 1, 2, 3, 4])
