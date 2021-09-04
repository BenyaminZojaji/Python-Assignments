userInputList=list(map(int, input().split()))
copyUserL=userInputList.copy()
userInputList.sort()
print('yes') if userInputList==copyUserL else print('no')
