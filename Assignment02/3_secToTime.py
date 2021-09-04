sec=int(input())
timeList=[]
timeList.append(sec//3600)
timeList.append((sec%3600)//60)
timeList.append((sec%3600)%60)
timeList=list(map(lambda x: str(x) if x>9 else '0'+str(x),timeList))
print(':'.join(timeList))
