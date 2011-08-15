
# n is abundant if the sum of it's proper divisors is greater than n
def proper_divisors(n):
  if n <= 1:  return
  yield 1
  for i in range(2, int(n ** .5) + 1):
    if n % i == 0:
      yield i
      if n / i != i:  yield n / i
def is_abundant(n):  return sum(proper_divisors(n)) > n

# Find abundants.  Find all possible sums.  Find non-matching numbers.
abunds = []
for i in range(28124):
  if is_abundant(i):  abunds.append(i)
target_nums = set()
for i in range(len(abunds)):
  if i % 100 == 0:  print i,
  for j in range(i, len(abunds)):
    target_nums.add(abunds[i] + abunds[j])
sum_ = 0
for n in range(28124):
  if n not in target_nums:
    sum_ += n
print sum_