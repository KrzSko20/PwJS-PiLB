import cmath


def main():
    a, b, c = input("a, b, c: ").split()
    a = int(a)
    b = int(b)
    c = int(c)
    print("Entered function: y = " + str(a) + "*x^2 + " + str(b) + "*x + " + str(c))

    delta = b * b - 4 * a * c

    if delta > 0:
        delta_sqrt = cmath.sqrt(delta)
        x1 = ((-b) - delta_sqrt) / (2 * a)
        x2 = ((-b) + delta_sqrt) / (2 * a)
        print("Function has 2 real roots: x1 = " + str(x1) + " and x2 = " + str(x2))

    elif delta == 0:
        x0 = (- b) / (2 * a)
        print("Function has 1 real root: x0 = " + str(x0))
    else:
        print("Function has no real roots")


if __name__ == '__main__':
    main()
