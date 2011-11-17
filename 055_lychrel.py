
from math import ceil

def is_palin(s):
    return s[:len(s) / 2] == s[-(len(s) / 2):][::-1]

def is_lychrel(num):
    for i in range(50):
        num = num + int(str(num)[::-1])
        if is_palin(str(num)):
            return False
    return True

print is_lychrel(196), is_lychrel(197), is_lychrel(4994)
print len([True for i in range(1, 10 ** 4) if is_lychrel(i)])