
s = ''.join([str(i) for i in range(1, 10 ** 6)])  
prod = 1
for i in range(7):
  prod *= int(s[10 ** i - 1])
print 'prod:', prod