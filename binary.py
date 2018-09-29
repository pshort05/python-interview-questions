#!/bin/python
""""
Task 
Given a base-10 integer,n , convert it to binary (base-2). Then find and print the base-20 integer denoting the maximum 
number of consecutive 1's in n's binary representation.

Input Format

A single integer, n.


Output Format

Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

Sample Case 1: 
The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.

Sample Case 2: 
The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.

""""

import sys

n = int(raw_input().strip())

binary = bin(int(n))[2:]
print binary
counter = 1
max = 0

for i in range(0, len(binary)):
    if binary[i] == 1:
        if counter == 0:
            counter = 1
        else:
            if binary[i - 1] == 1:
                counter += 1
    else:
        if counter > max:
            max = counter
        else:
            counter = 0

print max
