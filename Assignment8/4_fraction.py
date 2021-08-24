import re
def sum(x, y):
    result = {}
    result['s'] = x['s'] * y['m'] + x['m'] * y['s']
    result['m'] = x['m'] * y['m']
    return result
def sub(x, y):
    result = {}
    result['s'] =  x['s'] * y['m'] - x['m'] * y['s']
    result['m'] = x['m'] * y['m']
    return result
def mul(x, y):
    result = {}
    result['s'] = x['s'] * y['s']
    result['m'] = x['m'] * y['m']
    return result
def div(x, y):
    result = {}
    result['s'] = x['s'] * y['m']
    result['m'] = x['m'] * y['s']
    return result
def show(x):
    return str(x['s'])+'/'+str(x['m'])
a = {}
b = {}
aList= list(map(int, re.sub(r'^(\d+)/(\d+)', '\g<1>\g<2>', input('give me fraction1: e.g. 3/5\n'))))
bList= list(map(int, re.sub(r'^(\d+)/(\d+)', '\g<1>\g<2>', input('give me fraction2: e.g. 3/5\n'))))
a = {'s':aList[0],'m':aList[1]}
b = {'s':bList[0],'m':bList[1]}
print('sum: %s\tsub: %s\tmul: %s\tdiv: %s'%(show(sum(a, b)), show(sub(a, b)), show(mul(a, b)), show(div(a, b))))
