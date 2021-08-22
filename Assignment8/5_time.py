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
t1 = {'h':2, 'm':30, 's':45}
t2 = {'h':3, 'm':17, 's':40}
print('sum: %s\tsub: %s\ttimeToSec: %s\tsecToTime: %s'%(show(sum(t1, t2)), show(sub(t1, t2)), timeToSec(t1), show(secToTime(2000))))