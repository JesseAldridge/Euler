
def combos(n, k):
  ntok = 1
  for x in range(min(k, n-k)):
    ntok = ntok * (n-x) / (x+1)
  return ntok

count = 0
for n in range(1, 101):
    for k in range(1, n):
        if combos(n, k) > 10 ** 6:
            count += 1
print count