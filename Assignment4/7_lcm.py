def gcd(x, y):
    while y:
        x, y = y, x%y
    return x
def lcm(x, y):
    return x*y/gcd(x, y)
numbers = list(map(int, input('two numbers pls: e.g. 3 6\n').split()))
print(lcm(numbers[0], numbers[1]))