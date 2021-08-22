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
a['s']= int(input('a numered: '))
a['m']= int(input('a denumered: '))
b['s']= int(input('b numered: '))
b['m']= int(input('b denumered: '))
print('sum: %s\tsub: %s\tmul: %s\tdiv: %s'%(show(sum(a, b)), show(sub(a, b)), show(mul(a, b)), show(div(a, b))))