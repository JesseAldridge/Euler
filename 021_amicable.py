      
def proper_divisors(n):
  yield 1
  for i in range(2, int(n ** .5) + 1):
    if n % i == 0:
      yield i
      if n / i != i:  yield n / i
      
def sum_of_prop_divs(n):  return sum([i for i in proper_divisors(n)])
def is_amicable(n):
  sum_ = sum_of_prop_divs(n)
  return n != sum_ and n == sum_of_prop_divs(sum_)

sum_ = 0
for i in range(10000):
  if is_amicable(i):  sum_ += i
print sum_