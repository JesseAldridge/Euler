
from itertools import count
from collections import defaultdict

sigs = defaultdict(list)
for i in count():
    cube = i ** 3
    print i, cube
    sig = ''.join(sorted(str(cube)))
    sigs[sig].append(cube)
    if len(sigs[sig]) == 5:
        print sigs[sig]
        break