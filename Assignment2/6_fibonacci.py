n=int(input())
fiboList=[]
for i in range(n):
    if i < 2:
        fiboList.append(1)
    else:
        fiboList.append(fiboList[i-1]+fiboList[i-2])
print(','.join(list(map(str, fiboList))))