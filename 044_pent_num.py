
def pent_num(n):  
  return n * (3 * n - 1) / 2

pentas = []
pent_set = set()
min_diff = None
i = 0
while True:
  i += 1
  for j in range(1, i):
    pi, pj = pent_num(i), pent_num(j)
    diff = abs(pi - pj)
    if min_diff and diff > min_diff:
      break
    for x in (pi + pj, diff):
      while not pentas or x > pentas[-1]:
        new_penta = pent_num(len(pentas) + 1)
        pentas.append(new_penta)
        pent_set.add(new_penta)
      if x not in pent_set:
        break
    else:
      min_diff = diff
      print i, j, min_diff