import random


def integral():
    n = 100000
    count = 0

    x_min, x_max = 0.0, 1.0
    y_min, y_max = 0.0, 1.0

    for i in range(0, n):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)

        if x*x > y:
            count += 1

    integral_value = count / float(n)
    print(integral_value)


integral()
