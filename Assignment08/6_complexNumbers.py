import re
def sum(x, y):
    result = {}
    result['r']=x['r']+y['r']
    result['i']=x['i']+y['i']
    return result
def sub(x, y):
    result = {}
    result['r']=x['r']-y['r']
    result['i']=x['i']-y['i']
    return result
def mul(x, y):
    result = {}
    result['r']=x['r']*y['r']-x['i']*y['i']
    result['i']=x['i']*y['r']+x['r']*y['i']
    return result   
def show(x):
    return str(x['r'])+'+('+str(x['i'])+')i'
c1list = list(map(int, re.sub(r'^(\d+)[\+ \-](\d+)i$', '\g<1>\g<2>', input('complex number1: e.g. 2+3i\n'))))
c2list = list(map(int, re.sub(r'^(\d+)[\+ \-](\d+)i$', '\g<1>\g<2>', input('complex number2: e.g. 2+3i\n'))))
c1 = {'r':c1list[0], 'i':c1list[1]}
c2 = {'r':c2list[0], 'i':c2list[1]}
print('sum: %s\tsub: %s\tmul: %s'%(show(sum(c1, c2)), show(sub(c1, c2)), show(mul(c1, c2))))
