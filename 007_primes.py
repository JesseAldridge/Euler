
def is_prime(n):
  if n <= 1:  return False
  for i in range(2, int(n ** .5) + 1):
    if n % i == 0:  return False
  return True
  
# Find the 10001st prime number.
count = 0
n = 2
while True:
  if is_prime(n):  
    if count % 100 == 0:  print count,
    count += 1
  if count == 10001:
    print
    print 'answer: ', n
    break
  n += 1