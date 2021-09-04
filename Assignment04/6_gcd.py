def gcd(x, y):
    while y:
        x, y = y, x%y
    return x
numbers = list(map(int, input('two numbers pls: e.g. 3 6\n').split()))
print(gcd(numbers[0], numbers[1]))
