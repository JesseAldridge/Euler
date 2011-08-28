
# Generate palindromes < 10 ** 6.  Check whether they are palins in base 2.
palins = [i for i in range(1, 10)] + [i * 11 for i in range(1, 10)]
for i in range(10, 1000):
  str_i = str(i)
  palins += [int(str_i + s[::-1]) for s in (str_i[:-1], str_i)]
    
sum_ = 0
for palin in palins:
  if bin(palin)[2:] == bin(palin)[2:][::-1]:
    sum_ += palin
print 'sum:', sum_
