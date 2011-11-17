
n = 100

sum1 = (n * (n + 1) / 2) ** 2

print 'sum2:', (n ** 2 * (n + 1) ** 2 / 4) ** 4

sum2 = 0
for i in range(1, n + 1):
  sum2 += i ** 2  
print 'sum2:', sum2
print sum1 - sum2