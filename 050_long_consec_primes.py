
def primes(n):
  ## http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
  """ rwh_primes;  Returns  a list of primes < n """
  sieve = [True] * n
  for i in xrange(3, int(n ** 0.5) + 1, 2):
      if sieve[i]:
        sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

prime_list = primes(10 ** 7)
prime_set = set(prime_list)
  
stop_after = 10 ** 6
max_sum, max_len = 0, 0
for i in range(len(prime_list)):
  sum_ = 0
  j = i
  while True:
    sum_ += prime_list[j]
    if sum_ > stop_after:  break
    if sum_ in prime_set and (j - i) > max_len:
      print 'new max:', sum_
      max_sum = sum_
      max_len = j - i
    j += 1
print 'final max:', max_sum