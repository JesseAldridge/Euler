
from itertools import permutations


def primes(n):
  """ rwh_primes;  Returns  a list of primes < n """
  sieve = [True] * n
  for i in xrange(3, int(n ** 0.5) + 1, 2):
      if sieve[i]:
        sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

primes_ = set(primes(10 ** 7))
print 'got primes'
count = 0
for i in range(2, 10 ** 6):
  if i not in primes_:  continue
  digits = [ch for ch in str(i)]
  for _ in range(len(digits) - 1):
    digits.insert(0, digits.pop())
    if not int(''.join(digits)) in primes_:
      break
  else:
    print 'circular prime:', i
    count += 1
print 'final count:', count