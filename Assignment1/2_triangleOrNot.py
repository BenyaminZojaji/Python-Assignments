a, b, c=map(int, input('give me three sides: ').split())
if a<b+c and b<a+c and c<a+b:
    print('This triangle is drawable! Hooray!')
else:
    print('You can\'t draw a triangle with these sides, bilieve me!')