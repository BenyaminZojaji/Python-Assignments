n = int(input('Enter number of rows: '))
stars = 1 
for i in range(n):
    for j in range(n-i-1):
        print(end=' ')
    for k in range(stars):
        print('*', end='')
    stars+=2
    print()
stars = n*2-3
for i in range(1, n):
    for j in range(0, i):
        print(end=' ')
    for k in range(stars):
        print('*', end='')
    stars-=2
    print()