def fib(n):
    c1=0
    c2=1
    for i in range(0,n+1):
        c3=c1
        c1=c2
        c2=c1+c3
        print('fib(',i,')=',c3)
n=int(input('informe um número:'))
fib(n)

