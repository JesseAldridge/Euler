
# 1 1 2 3 5 8 13 ...  with memoization
mem = {}
def fib(n):
  if n <= 0:  raise Exception
  if n <= 2:  return 1
  if n not in mem:  mem[n] = fib(n - 1) + fib(n - 2)
  return mem[n]
  
# Find the sum of all even results < 4 million.
sum_ = 0
n = 1
while True:
  result = fib(n)
  if result > 4 * 10 ** 6:  break
  if result % 2 == 0:  sum_ += result
  n += 1
print 'sum: ', sum_
  