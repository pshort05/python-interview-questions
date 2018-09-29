

def pascal(r, c):
    if c<0 and r<0:
        return 0
    if c==0 and r==0:
        return 1
    else:
        return pascal(r-1,c) + pascal(r-1,c-1)


print pascal(2,1)
