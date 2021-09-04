from math import mean
name, family=input().split()
g1, g2, g3 = input().split()
avg = mean(float(g1), float(g2), float(g3))
if avg<12:
    print('Fail')
elif avg<17:
    print('Normal')
else:
    print('Great')
