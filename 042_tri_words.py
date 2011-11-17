
def tri(n):  return n * (n + 1) / 2

# Build set of triangle nums as needed.

class g:
  tri_nums = set()
  max_tri_num = 0
  n_tri = 1
  
def is_tri_num(n):
  while g.max_tri_num < n:
    g.max_tri_num = tri(g.n_tri)
    g.tri_nums.add(g.max_tri_num)
    g.n_tri += 1
  return n in g.tri_nums
  

# Read word file, count all triangle words.

def is_triangle_word(s):
  sum_ = 0
  for ch in s:
    sum_ += ord(ch) - ord('A') + 1
  return is_tri_num(sum_)
    
with open('words.txt') as f:  
  words = [word[1:-1] for word in f.read().split(',')]

count = 0
for word in words:
  if is_triangle_word(word):
    count += 1
print 'count:', count