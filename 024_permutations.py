
from itertools import permutations

for i, p in enumerate(permutations('0123456789')):
  if i == 10 ** 6 - 1:
    print p