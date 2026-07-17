def reverse1( x):
    negative = False
    if x < 0:
        negative = True
        x = -(x)
    y = 0
    while x != 0:
        s = x % 10
        y = (s*10) + s

    if negative:
        y = -(y)
        return y
    return y

print(reverse1(123))

