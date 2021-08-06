def snakeAssembler(n):
    while n!=0:
        yield '*'
        n-=1
        if n==0:break
        yield '#'
        n-=1
print(''.join(list(snakeAssembler(int(input())))))