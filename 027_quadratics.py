
# Find the denominator n < 1000 which has the longest decimal cycle for 1 / n.
remainders = set()
max_len = 0
for denom in range(1, 1000):
  remainders = set()
  cycle_n = 1
  while True:
    remainder = 10 ** cycle_n % denom
    if remainder in remainders:
      cycle = str(10 ** cycle_n / denom)
      if len(cycle) > max_len:  
        max_denom, max_len = denom, len(cycle)
      break
    remainders.add(remainder)
    cycle_n += 1
print max_denom