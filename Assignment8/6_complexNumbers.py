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

c1 = {'r':5, 'i':3}
c2 = {'r':7, 'i':1}
print('sum: %s\tsub: %s\tmul: %s'%(show(sum(c1, c2)), show(sub(c1, c2)), show(mul(c1, c2))))