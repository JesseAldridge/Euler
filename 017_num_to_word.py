
import inflect
p = inflect.engine()
s = ''
for i in range(1, 1001):  s += p.NUMWORDS(i)
s = s.replace(' ', '').replace('-', '').replace(',', '')
print len(s)