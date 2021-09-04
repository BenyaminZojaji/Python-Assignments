from statistics import mean
scoreList=[]
n=int(input())
for i in range(n):
    scoreList.append(float(input()))
scoreList.sort()
print('Mean: %f ,Max: %f ,Min: %f' %(mean(scoreList), scoreList.pop(), scoreList[0]))
