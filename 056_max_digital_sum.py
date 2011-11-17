
sums = []
for a in range(100):
    for b in range(100):
        sums.append(sum([int(ch) for ch in str(a ** b)]))
print max(sums)