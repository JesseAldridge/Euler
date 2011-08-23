
'''
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
'''
grid_width = 1001
curr_num = 1
sum_ = 1
for cycle in range(2, grid_width, 2):
  for i in range(4):
    curr_num += cycle
    sum_ += curr_num
print sum_
