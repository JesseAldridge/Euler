
x = 1
while True:
    for i in range(2, 7):
        if set(str(x)) != set(str(x * i)):
            break
    else:
        print x
        break
    x += 1