
def proper_divisors(n):
  for i in range(1, n):
    if n % i == 0:
      yield i
      
def sum_of_pds(n):  return sum([i for i in proper_divisors(n)])
def is_amicable(n):
  sum_ = sum_of_pds(n)
  return n != sum_ and n == sum_of_pds(sum_)

sum_ = 0
for i in range(10000):
  if i % 100 == 0:  print i,
  if is_amicable(i):  sum_ += i
print sum_