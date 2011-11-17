
def gen_primes():
  ## http://stackoverflow.com/questions/567222/simple-prime-generator-in-python
  D = {}  
  q = 2  

  while True:
    if q not in D:
      yield q    
      D[q * q] = [q]
    else:
      for p in D[q]:
        D.setdefault(p + q, []).append(p)
      del D[q]
    q += 1
 
# Find the eleven truncatable primes.
primes = set()
count = 0
sum_ = 0
for prime in gen_primes():
  primes.add(prime)
  if prime <= 7:  continue
  sprime = str(prime)
  for i in range(1, len(sprime)):
    if int(sprime[i:]) not in primes:  break
    if int(sprime[:-i]) not in primes:  break
  else:
    count += 1
    sum_ += prime
    if count >= 11:
      break
print 'sum:', sum_