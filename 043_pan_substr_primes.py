
from itertools import permutations

def all_unique(l):
  seen = set()
  for x in l:
    if x in seen:
      return False
    seen.add(x)
  return True

# Last 3 digits are a multiple of 17 with no repeated digits.
last_3_i = 0
sum_ = 0
while last_3_i < 999:
  last_3_i += 17
  last_3_str = str(last_3_i)
  if last_3_i < 100:
    last_3_str = '0' + last_3_str
  if not all_unique(last_3_str):
    continue
    
  # Permute remaining; find perms that have substrs divisible in the right way.
  for p in permutations(set('1234567890') - set(last_3_str)):
    p += tuple(last_3_str)
    if int(p[3]) % 2 != 0 or int(p[5]) % 5 != 0:  continue
    if sum([int(digit) for digit in p[2:5]]) % 3 != 0:  continue
    for i, prime in enumerate([7,11,13]):
      if int(''.join(p[i + 4:i + 7])) % prime != 0:
        break
    else:
      sum_ += int(''.join(p))
      
print 'sum:', sum_