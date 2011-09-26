
import os
from itertools import combinations

from jca.misc.primes import primes, is_prime
  

# For each prime (eg 13), replace each digit with a wildcard (eg *3, 1*).
def go():
  checked = set()
  for prime in primes(10 ** 6):
    prime_str = str(prime)
    for prime_char in set(prime_str):
      wild_str = prime_str.replace(prime_char, '*')
      if wild_str in checked:  continue
      checked.add(wild_str)

      # Replace each wildcard with a digit.
      matches = []
      for new_digit in range(10):
        new_str = wild_str.replace('*', str(new_digit))
        if new_str[0] == '0':  continue
        if is_prime(int(new_str)):
          matches.append(int(new_str))
      if len(matches) == 8:
        return matches
print go()