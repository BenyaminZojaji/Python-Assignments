n = int(input())
triangleList = []
for i in range(n):
    temp = []
    if i == 0:
        temp.append(1)
    else:
        for j in range(i+1):
            if j==0 or j==i:
                temp.append(triangleList[i-1][j-1])
            else:
                temp.append(triangleList[i-1][j]+triangleList[i-1][j-1])
    triangleList.append(temp)
for i in range(n):
    for j in range(i+1):
        print(triangleList[i][j], end=' ')
    print()
