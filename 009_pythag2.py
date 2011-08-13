
from math import sqrt, ceil

def gcd(a, b):
  """Return greatest common divisor using Euclid's Algorithm."""
  while b:      
    a, b = b, a % b        
  return a

# Find primitive a + b + c == total where a + b + c == 2 * m * (m + n) * d.
def pythag_trip(total):
  half_total = total / 2
  for m in range(2, int(ceil(sqrt(half_total))) - 1):
    if half_total % m == 0:
      total_over_2m = half_total / m
      while total_over_2m % 2 == 0:
        total_over_2m /= 2
        
      # (a + b + c) / 2m == (m + n);  0 < n < m;  only one of {n,m} is even
      m_plus_n = m + 2 if m % 2 == 1 else m + 1
      while m_plus_n < 2 * m and m_plus_n <= total_over_2m:
        if total_over_2m % k == 0 and gcd(k, m) == 1:
          d = half_total / (k * m)
          n = k - m
          a = d * (m * m - n * n)
          b = 2 * d * m * n
          c = d * (m * m + n * n)
          return a * b * c
        k += 2
for i in range(1, 100):
  print i, pythag_trip(i)