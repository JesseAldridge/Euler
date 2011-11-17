
from pprint import pprint

'''
17 16 15 14 13
18  5  4  3 12
19  6  1  2 11
20  7  8  9 10
21 22 23 24 25
'''

def is_prime(n):
  if n <= 1:  return False
  if n == 2:  return True
  if n % 2 == 0:  return False
  for i in range(3, int(n ** .5) + 1, 2):
    if n % i == 0:
      return False
  return True

# For each layer:  Move dist to find primes to non-prime ratio on diagonals.
dist = 2
cell_count = 1
prime_count = 0
while True:
    for i in range(4):
        cell_count += dist
        if is_prime(cell_count):
            prime_count += 1
    size = dist + 1
    dist += 2
    ratio = prime_count / float(size * 2 - 1)
    if ratio < .1:
        break

print 'final size:', size
