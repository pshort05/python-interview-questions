def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def fibonacci(n):
    f=0
    next=1
    step=0
    for i in range(0,n):
        step=f
        f=next
        next+=step
        print f,
    return f


print fibonacci(1)
print fibonacci(2)
print fibonacci(3)
print fibonacci(4)
print fibonacci(5)
print fibonacci(6)
print fibonacci(7)
print fibonacci(8)
