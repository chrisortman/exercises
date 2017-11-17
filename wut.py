def main():

    print(f(13))


def f(x):
    print("Invoke f with",x)
    y = g(x)
    print("y=", y)
    z = h(x,y)
    print("z=", z)
    return j(g(y+z), x)

def g(x):
    a = j(h(x+x, x), x)
    b = h(x*2, a)
    c = ff(a, x)
    d = ff(x-b, 9)
    return c

def h(x,y):
    print("Got",x,y)
    a = x % 3
    b = y
    y = a
    x = b**2
    for x in range(a,b):
        y = x + y

    return y

def j(x,y):
    try:
        if x % 2 == 0:
            return floor(x / y)
        else:
            return y * 2
    except:
        return x + y

def ff(x,y):
    a = 0
    for i in range(x,y):
        c = 10
        d = 6
        e = 8
        if (x*y+i) % 4 == 0:
            a += x + c
        elif i > y:
            a += y * d
        elif (x - y) == 1:
            a += x + y
        else:
            a += x - y

        d += 1
    return a


main()
