t = int(input())
if 0<t<101:
    p = (int)(1e1)
    for i in range(t):
        a,b = 1,1
        m = int(input())
        if 0<m<10**9:
            for j in range(m):
                a,b=b,a+b
                mod = pow(a,1,p)
            print(mod)