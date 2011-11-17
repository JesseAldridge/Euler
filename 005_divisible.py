
def lcm(*args):
  if len(args) > 2:  return lcm(args[0], lcm(*args[1:]))
  return args[0] * args[1] /  gcd(args[0], args[1])

def gcd(a, b):
  while b:  a, b = b, a % b        
  return a

print lcm(*[i for i in range(1, 21)])