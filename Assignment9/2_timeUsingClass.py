class Time:
    def __init__(self, hour=None, minute=None, second=None):
        self.hour = hour
        self.minute = minute
        self.second = second
    def sum(self, time):
        result = Time()
        result.second = self.second + time.second
        result.minute = self.minute + time.minute
        result.hour = self.hour + time.hour
        if result.second>=60:
            result.second-=60
            result.minute+=1
        if result.minute>=60:
            result.minute-=60
            result.hour+=1
        return result
    def sub(self, time):
        result = Time()
        result.second = self.second - time.second
        result.minute = self.minute - time.minute
        result.hour = self.hour - time.hour
        if result.second<0:
            result.minute-=1
            result.second+=60
        if result.minute<0:
            result.hour-=1
            result.minute+=60
        return result
    def secToTime(self):
        result = Time()
        result.hour = self.second//3600
        result.minute = (self.second%3600)//60
        result.second = (self.second%3600)%60
        return result
    def timeToSec(self):
        return self.hour*3600 + self.minute*60 + self.second
    def show(self):
        return str(self.hour)+':'+str(self.minute)+':'+str(self.second)
t1list = list(map(int, input('time1: e.g. 2:16:18\n').split(':')))
t2list = list(map(int, input('time2: e.g. 2:16:18\n').split(':')))
sec = Time(0 ,0 ,int(input('give me sec convert to time: ')))
t1 = Time(t1list[0], t1list[1], t1list[2])
t2 = Time(t2list[0], t2list[1], t2list[2])
print('sum: %s\tsub: %s\ttimeToSec: %s\tsecToTime: %s'%((t1.sum(t2)).show(), t1.sub(t2).show(), t1.timeToSec(), (sec.secToTime()).show()))