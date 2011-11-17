
from itertools import permutations

def primes(n):
  sieve = [True] * n
  for i in xrange(3, int(n ** 0.5) + 1, 2):
      if sieve[i]:
        sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]
  
prime_list = primes(10 ** 4)
prime_set = set(prime_list)

for prime_int in prime_list:
  if prime_int < 1000:  continue
  prime_str = str(prime_int) 
  prime_perms = []
  for perm_str in permutations(prime_str):
    if perm_str[0] == '0':  continue
    perm_int = int(''.join(perm_str))
    if perm_int in prime_set and not perm_int in prime_perms:
      prime_perms.append(perm_int)
  pp = prime_perms
  for i in range(1, len(pp)):
    for j in range(i + 1, len(pp)):
      if pp[i] - pp[0] == pp[j] - pp[i]:
        print pp[0], pp[i], pp[j]
  