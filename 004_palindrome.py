
# Find the largest palindrome made from the product of two 3-digit numbers.
palins = []
for x in range(100, 1000):
  for y in range(100, 1000):
    s = str(x * y)
    if s == s[::-1]:
      palins.append(x * y)
print max(palins)