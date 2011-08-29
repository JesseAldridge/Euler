
## Better solution:  http://www.thattommyhall.com/2008/04/12/project-euler-39/

max_sols_p, max_sols = 0, 0
for p in range(3, 1000):
  print p,
  num_solutions = 0
  
  for a in range(1, (p - 3) / 3):
    for b in range(a, (p - a) / 2):
      c = p - a - b
      if a ** 2 + b ** 2 == c ** 2:
        num_solutions += 1
  if num_solutions > max_sols:
    max_sols = num_solutions
    max_sols_p = p
print
print 'p:', max_sols_p, 'num solutions:', max_sols