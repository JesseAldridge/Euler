
def lcm(*args):
  if len(args) > 2:  return lcm(args[0], lcm(*args[1:]))
  return args[0] * args[1] /  gcd(args[0], args[1])

def gcd(a, b):
  while b:  a, b = b, a % b
  return a

# Find the smallest number evenly divisible by every number in 1 through 21.
print lcm(*[i for i in range(1, 21)])
print 232792560 % 21, 232792560 % 20, 232792560 % 19