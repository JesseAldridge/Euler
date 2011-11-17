
def prime_factors(n):
  if n == 1:  return [1]
  for i in range(2, int(n ** .5) + 1):
    if n % i == 0:
      return [i] + prime_factors(n / i)
  return [n, 1]
  
print prime_factors(600851475143)