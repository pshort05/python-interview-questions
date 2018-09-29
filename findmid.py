#!/bin/python

import sys


n = int(raw_input().strip())
a = []
a_i = 0
#mid1=0
#mid2=0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)
    a.sort()
    if a_i==0:
        print a[0]*1.0
    else:
        if len(a)%2:
            mid1 = len(a)/2
            mid2 = mid1
        else:
            mid1 = (len(a)/2) - 1
            mid2 = mid1+1
        print (a[mid1]+a[mid2])/2.0
        #print len(a), a, len(a), len(a)/2, len(a)%2, "|", mid1, mid2
