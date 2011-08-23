
n = 100
results = set()
for a in range(2, n + 1):
  for b in range(2, n + 1):
    results.add(a ** b)
print len(results)