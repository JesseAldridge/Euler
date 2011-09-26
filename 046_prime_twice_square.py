
import math

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?  15 = 7 + 2 * 2 ** 2

def primes(n):
  """ rwh_primes;  Returns  a list of primes < n """
  sieve = [True] * n
  for i in xrange(3, int(n ** 0.5) + 1, 2):
      if sieve[i]:
        sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

prime_list = primes(10 ** 5)
prime_set = set(prime_list)
        
n = 1
while True:
  found = False
  for prime in prime_list:
    if prime >= n:  break
    res = math.sqrt((n - prime) / 2)
    if res == int(res):
      found = True
      break
  if not found:
    print n
  while True:
    n += 2
    if n not in prime_set:
      break