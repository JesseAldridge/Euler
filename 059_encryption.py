
from collections import defaultdict
from operator import itemgetter
from itertools import cycle

# Read the bytes.
with open('059_cipher1.txt') as f:
    coded_ints = f.read().strip().split(',')
coded_ints = [int(i) for i in coded_ints]

def sorted_count(list_):
    ' Sort list by commonality (most common item comes first). '
    d = defaultdict(int)
    for coded_int in list_:
        d[coded_int] += 1
    return [x[0] for x in sorted(d.iteritems(), key=itemgetter(1),
                                 reverse=True)]

def each_pass():
    ' Generate each possible password. '
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    for first in alphas:
        for second in alphas:
            for third in alphas:
                yield first + second + third

# Try decoding the data with each password.  Check if the result makes sense.
for password in each_pass():
    decoded_chars = []
    for coded_int, pass_ch in zip(coded_ints, cycle(password)):
        decoded_chars.append(chr(coded_int ^ ord(pass_ch)))
    decoded_str = ''.join(decoded_chars)
    most_common = sorted_count(decoded_str)

    # Used to get the hint (also need to take out the break below)
    # if most_common[0] == ' ' and most_common[1] == 'e':

    # Used to get the answer
    if 'The Gospel' in decoded_str:

        print 'pass:', password
        print 'decoded:', decoded_str
        break

print 'sum:', sum([ord(ch) for ch in decoded_chars])