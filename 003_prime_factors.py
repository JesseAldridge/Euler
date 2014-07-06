
import operator

def prime_factors(n):
  
  # Recursively divide n by the smallest factor that divides it evenly.
  
  if n == 1:  
    return [1]
  for i in range(2, int(n ** .5) + 1):
    if n % i == 0:
      return [i] + prime_factors(n / i)
  return [n, 1]

print prime_factors(600851475143)
print reduce(operator.mul, prime_factors(600851475143))
