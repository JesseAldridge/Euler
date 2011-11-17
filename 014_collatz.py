  
# Iterate n.  Look to see if we've already solved the sub-problem.  
mem = {}
def chain_len(start):
  chain = [start]
  n = start
  chain_len_ = 1
  while n > 1:
    if n in mem:  
      chain_len_ += mem[n]
      break
    else:  chain_len_ += 1
    n = n / 2 if n % 2 == 0 else 3 * n + 1
  mem[start] = chain_len_
  return mem[start]

# Find biggest chain.
max_n, max_len = 0, 0
for n in range(1, 10 ** 6):
  if n % 10000 == 0:  print n,
  chain_len_ = chain_len(n)
  if chain_len_ > max_len:  
    max_len = chain_len_
    max_n = n
print
print 'max_n: ', max_n