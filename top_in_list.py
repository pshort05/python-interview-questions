#!/usr/bin/python

"""""
Given a list of integers, print the top k values in the list
"""""
import heapq
import random
from timeme import timeme


@timeme
def top_values(input_list, top_number):
    # copy list to local variable so we don't modify the original list
    tmp_list = input_list
    # for better performance replace sort
    tmp_list.sort()
    # check that the top selection is not larger than the list
    cnt = len(tmp_list)
    if top_number > cnt:
        k = cnt
    else:
        k = top_number

    return tmp_list[cnt:cnt-k-1:-1]


@timeme
def heapSearch( bigArray, k ):
    heap = []
    # Note: below is for illustration. It can be replaced by
    # heapq.nlargest( bigArray, k )
    for item in bigArray:
        # If we have not yet found k items, or the current item is larger than
        # the smallest item on the heap,
        if len(heap) < k or item > heap[0]:
            # If the heap is full, remove the smallest element on the heap.
            if len(heap) == k: heapq.heappop( heap )
            # add the current element as the new smallest.
            heapq.heappush( heap, item )
    return heap

@timeme
def heaplargest(bigarray, k):
    return heapq.nlargest(bigarray, k)

# Test Cases

print top_values([2,3,4,5,6,7,8], 2)
print top_values([0,4,1,9,34,22,14,993,2,43444,23,52,134,1], 5)

# create a larger list for performance testing
biglist=[]
random.seed()
for k in range(0,1000000):
    biglist.append(random.randint(0,10000000))

# Interesting time results
print top_values(biglist, 10)
print heapSearch(biglist, 10)
print heaplargest(10, biglist)
