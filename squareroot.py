# Calculate a square root without using the square root function
# Note:  using an approximation method

from math import sqrt

def squareroot(x):

    if x<= 0:
        return 0

    high = (x+1)/2.0
    low = 0.0
    mid = (high+low)/2.0

    for i in range(0, 100):
        if mid*mid > x:
            high = mid
        elif mid*mid == x or mid==high:
            print i,
            return mid
        else:
            low = mid
        mid = (high+low)/2.0
    return mid


print squareroot(1.0), sqrt(1.0)
print squareroot(100.0), sqrt(100.00)
print squareroot(4.0), sqrt(4.0)
print squareroot(10.0), sqrt(10.0)
print squareroot(.5), sqrt(.5)
