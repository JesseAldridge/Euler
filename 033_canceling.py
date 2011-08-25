
# num[1] == denom[0] and num / denom == num[0] / denom[1];  eg 49 / 98 = 4 / 8
final_num, final_denom = 1, 1
for num in range(11, 100):
  for denom in range(num + 1, 100):
    if denom % 10 == 0:  continue
    if str(num)[1] != str(denom)[0]:  continue
    if float(num) / float(denom) == float(str(num)[0]) / float(str(denom)[1]):
      print num, denom
      final_num *= num
      final_denom *= denom
      
print 'fraction:', final_num, '/', final_denom
print float(final_denom) / final_num