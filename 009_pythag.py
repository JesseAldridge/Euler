

# Find a**2 + b**2 == c**2 where a + b + c == n.
def find_pythag_trip(n):
  for a in range(1, (n - 3) / 3):
    for b in range(a, (n - a) / 2):
      c = n - a - b
      if a ** 2 + b ** 2 == c ** 2:
        return a, b, c
          
prod = 1
for x in find_pythag_trip(1000):  prod *= x
print prod