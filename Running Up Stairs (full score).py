t = int(input())
for i in range(t):
    a = 1
    b = 1
    fib = 1
    n = int(input())
    for j in range(n-1):
        fib = a + b
        a = b
        b = fib
    print (fib)