
from fractions import Fraction

f = Fraction(1, 2)
count = 0
for i in range(1000):
    f = 1 / (2 + f)
    f1 = 1 + f
    if len(str(f1.numerator)) > len(str(f1.denominator)):
        count += 1
print 'count:', count