
from itertools import permutations

def is_prime(n):
  if n <= 1:  return False
  for i in range(2, int(n ** .5) + 1):
    if n % i == 0:  return False
  return True

# Find biggest pandigital prime.
l = [1,2,3,4,5,6,7,8,9]
max_num = 0
while l:
  ## If sum(digits) % 3 == 0, the number is divisible by 3.
  if sum(l) % 3 != 0:
    for p in permutations(l):
      num = int(''.join([str(i) for i in p]))
      if is_prime(num):
        if num > max_num:
          max_num = num
  l.pop()
print 'max_num:', max_num