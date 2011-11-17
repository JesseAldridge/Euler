
def tri(n):  return n * (n + 1) / 2
def inv_tri(n):  return (-1 + (1 + 8 * n) ** .5) / 2
def pent(n):  return n * (3 * n - 1) / 2
def inv_pent(n):  return (1 + (1 + 24 * n) ** .5) / 6
def hex_(n):  return n * (2 * n - 1)

n = 1
while True:
  test = hex_(n)
  tri_ = inv_tri(test)
  if int(tri_) == tri_:
    pent_ = inv_pent(test)
    if int(pent_) == pent_:
      print test
  n += 1