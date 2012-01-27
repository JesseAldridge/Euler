
from itertools import combinations, permutations
from pprint import pprint

from jca.misc.primes import gen_primes, is_prime


def cat(a, b):  return int(str(a) + str(b))
def fits(a, b):  return is_prime(cat(a, b)) and is_prime(cat(b, a))

# Build a tree.

# 1 + 2 - 3
#   |
#   + - 3
#
# 2 - 3
#
# 3

primes = sorted(gen_primes(10**7))
nodes = []

class Node:
  def __init__(self, prime):
    self.prime = prime
    self.connections = []

  def add(self, prime, chain=None):
    if chain is None:  chain = []
    if fits(self.prime, prime):
      if len(chain) == 3:
        print 'winner:', chain + [self.prime, prime]
        print 'sum:', sum(chain + [self.prime, prime])
        return True
      elif len(chain) == 2:
        print 'almost:', chain + [self.prime, prime]
      for connection in self.connections:
        if connection.add(prime, chain + [self.prime]):
          return True
      self.connections.append(Node(prime))

def go():
  for prime in primes:
    for node in nodes:
      if node.add(prime):
        return
    nodes.append(Node(prime))
go()