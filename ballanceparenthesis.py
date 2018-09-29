#!/usr/bin/env python
# -*- coding: utf-8 -*-

OPEN = '('
CLOSED = ')'

# Returns # of unbalanced parenthesis
def is_balanced(string):
    open = 0
    close = 0
    for i in string:
        if i == OPEN:
            open += 1
            continue
        if i == CLOSED:
            if open > 0:
                open -= 1
            else:
                close -= 1
            continue
    return open, close

priornodes={}

def has_cycle(head):
    if head is None:
        return True
    if head in priornodes.keys():
        print('1')
        return False
    print('0')
    priornodes.update(head)
    return has_cycle(head.next)

prior_nodes={}
prior_nodes.

print is_balanced("(a(b-1)2)")
print is_balanced("(((((")
print is_balanced("))((")
print is_balanced("()(()))()")





