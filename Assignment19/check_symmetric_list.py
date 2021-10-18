arr = list(map(int, input().split()))
flag=True
for i in range(len(arr)):
    if arr[i]!=arr[len(arr)-1-i]:
        flag=False
        break
if flag:
    print('symmetric')
else:
    print('not symmetric')