def sum(x, y):
    result = {}
    result['s'] = x['s'] + y['s']
    result['m'] = x['m'] + y['m']
    result['h'] = x['h'] + y['h']
    if result['s'] >=60:
        result['s']-=60
        result['m']+=1
    if result['m'] >=60:
        result['m']-=60
        result['h']+=1
    if result['h']>23:
        result['h']-=24
    return result
def sub(x, y):
    result = {}
    result['s'] = x['s'] - y['s']
    result['m'] = x['m'] - y['m']
    result['h'] = x['h'] - y['h']
    if result['s']<0:
        result['m']-=1
        result['s']+=60
    if result['m']<0:
        result['h']-=1
        result['m']+=60
    return result
def timeToSec(x):
    return x['h']*3600 + x['m']*60 + x['s']
def secToTime(x):
    result = {}
    result['h'] = x//3600
    result['m'] = (x%3600)//60
    result['s'] = (x%3600)%60
    return result
def show(x):
    return str(x['h'])+':'+str(x['m'])+':'+str(x['s'])
t1list = list(map(int, input('time1: e.g. 2:16:18\n').split(':')))
t2list = list(map(int, input('time2: e.g. 2:16:18\n').split(':')))
sec = int(input('give me sec convert to time: '))
t1 = {'h':t1list[0], 'm':t1list[1], 's':t1list[2]}
t2 = {'h':t2list[0], 'm':t2list[1], 's':t2list[2]}
print('sum: %s\tsub: %s\ttimeToSec: %s\tsecToTime: %s'%(show(sum(t1, t2)), show(sub(t1, t2)), timeToSec(t1), show(secToTime(sec))))
