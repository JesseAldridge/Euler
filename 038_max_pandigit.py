
from math import factorial
from itertools import permutations

# Helpers

def all_unique(l):
  seen = set()
  for x in l:
    if x in seen:
      return False
    seen.add(x)
  return True
  
def is_pandigital(s):
  for ch in '123456789':
    if ch not in s:
      return False
  return True

# Start with 9.  Find cat product until repeat or too big.
  
test = 9
max_ = 0
while True:
  
  cat_prod = ''
  for i in range(1, 10):
    cat_prod += str(test * i)
    if len(cat_prod) >= 10 or not all_unique(cat_prod):
      break
  if len(cat_prod) >= 9:
    cat_prod = cat_prod[:9]
    
  # Store max pandigital.  Make sure test number starts with 9.
    
  if is_pandigital(cat_prod):
    if int(cat_prod) > max_:
      print 'new max, cat_prod:', cat_prod, 'test:', test
      max_ = int(cat_prod)
  
  test += 1
  if str(test)[0] != '9':
    test *= 9

  if len(str(test)) > 4:
    break
    
print 'max_:', max_