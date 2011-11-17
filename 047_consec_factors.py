
mem = {}
def prime_factors(n):
  if n == 1:  return [1]
  if n in mem:  return mem[n]
  for i in range(2, int(n ** .5) + 1):
    if n % i == 0:
      mem[n] = [i] + prime_factors(n / i)
      return mem[n]
  return [n]
  
# Find n consecutive numbers that each have n distinct prime factors
n = 4
x = 1
while True:
  factors = set()
  good = True
  for off in range(n):
    factors = set(prime_factors(x + off))
    if len(factors) != n:
      break
  else:
    print x
  x += 1