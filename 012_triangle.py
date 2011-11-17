
import time

# Get first 1000 primes.
def is_prime(n):
  if n <= 1:  return False
  for i in range(2, int(n ** .5) + 1):
    if n % i == 0:  return False
  return True
primes = []
n = 2
while True:
  if is_prime(n):  
    primes.append(n)
    if len(primes) > 1000:  break
  n += 1
  
print 'got primes'
  
# n == 2 ** a1 * 3 ** a2 * 5 ** a3 * ...;  
# num_divisors = (a1 + 1) * (a2 + 1) * (a3 + 1) * ...
def num_divisors(n):    
  exps = {}
  for prime in primes:
    exps[prime] = 0
    while n % prime == 0:
      n /= prime
      exps[prime] += 1
    if n == 1:  
      prod = 1
      for key in exps:  prod *= exps[key] + 1
      return prod
 
# Find first triangle number with > 500 divisors.
start = time.time()
def tri_nums():
  n = 1
  sum_ = 0
  while True:
    sum_ += n
    yield sum_
    n += 1
for i, n in enumerate(tri_nums()):
  if i % 1000 == 0:  print n,
  if num_divisors(n) > 500:
    print
    print 'answer: ', n
    break
print 'time: ', time.time() - start