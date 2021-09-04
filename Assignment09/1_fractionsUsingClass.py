class Fraction:
    def __init__(self, numerator=None, denumerator=None):
        self.numerator = numerator
        self.denumerator = denumerator
    def sum(self, frac):
        result = Fraction()
        result.numerator = self.numerator*frac.denumerator + self.denumerator*frac.numerator
        result.denumerator = self.denumerator*frac.denumerator
        return result
    def mul(self, frac):
        result = Fraction()
        result.numerator = self.numerator*frac.numerator
        result.denumerator = self.denumerator*frac.denumerator
        return result
    def div(self, frac):
        result = Fraction()
        result.numerator = self.numerator*frac.denumerator
        result.denumerator = self.denumerator*frac.numerator
        return result
    def sub(self, frac):
        result = Fraction()
        result.numerator = self.numerator*frac.denumerator - self.denumerator*frac.numerator
        result.denumerator = self.denumerator*frac.denumerator
        return result
    def show(self):
        return str(self.numerator) + '/' + str(self.denumerator)
aList= list(map(int, input('give me fraction1: e.g. 3/5\n').split('/')))
bList= list(map(int, input('give me fraction2: e.g. 3/5\n').split('/')))
a = Fraction(aList[0], aList[1])
b = Fraction(bList[0], bList[1])
print('sum: %s\tsub: %s\tmul: %s\tdiv: %s'%((a.sum(b)).show(), (a.sub(b)).show(), (a.mul(b)).show(), (a.div(b)).show()))
