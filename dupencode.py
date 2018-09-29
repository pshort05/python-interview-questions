#!/usr/bin/python


def encode(string):
    encoded = ""
    n = 1
    l = None
    for i in string:
        if i == l:
            n += 1
        else:
            if l:
                encoded += "{}{}".format(l, n)
            n = 1
            l = i
    encoded += "{}{}".format(l, n)
    return encoded

print encode("AAAAabIIIaII")
print encode('aaabbcddddeefa')