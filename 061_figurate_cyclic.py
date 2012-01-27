
# Figurate numbers forumlae.
formulae = [lambda n:  n * (n + 1) / 2,
            lambda n:  n * n,
            lambda n:  n * (3 * n - 1) / 2,
            lambda n:  n * (2 * n - 1),
            lambda n:  n * (5 * n - 3) / 2,
            lambda n:  n * (3 * n - 2)]

# Find all 4 digit numbers for each figurate type.
sets = []
for form in formulae:
    sets.append(set())
    i = 0
    while True:
        i += 1
        next = form(i)
        if next < 1000:
            continue
        if next > 9999:
            break
        sets[-1].add(next)

def one_from_each(so_far, sets):
    ' Pick one number from each set that is cyclic with the previous number. '
    if not sets:
        yield so_far
        return
    for i in range(len(sets)):
        for val in sets[i]:
            if not so_far or str(val)[:2] == str(so_far[-1])[-2:]:
                for new_list in one_from_each(so_far + [val],
                                              sets[:i] + sets[i + 1:]):
                    yield new_list


for l in one_from_each([], sets):
    if str(l[0])[:2] == str(l[-1])[-2:]:
        print l, sum(l)