
from itertools import permutations

# Does the number use each digit from one to it's length exactly once?
def is_pandigital(s):
  for i in range(1, len(s) + 1):
    if str(i) not in s:
      return False
  return True

# Find all matches.
products = set()
for x in range(1, 2000):
  for y in range(x, 2000):
    s = str(x) + str(y) + str(x * y)
    if(len(s) == 9 and is_pandigital(s)):
      print x, y, x * y
      products.add(x * y)
print 'final sum:', sum(products)