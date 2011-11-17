
mem = {}
def factorial(n):
  if n == 1 or n == 0:  return 1
  if n in mem:  return mem[n]
  mem[n] = factorial(n - 1) * n
  return mem[n]
  
nums = []
for n in range(3, 50000):
  sum_ = 0
  for digit in str(n):
    sum_ += factorial(int(digit))
  if sum_ == n:  nums.append(n)
print sum(nums)