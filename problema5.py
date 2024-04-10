import numpy as np


def f(x):
    return np.sum(x)


def isValid(x):
    return True if len(x) == 7 else False


def generare(dim):
    popg = []
    for _ in range(dim):
        valid = False
        while not valid:
            x1 = np.random.rand()
            x2 = np.random.rand()
            x3 = np.random.rand()
            x4 = np.random.rand()
            x5 = np.random.rand()
            x6 = np.random.rand()
            x7 = np.random.rand()

            x = [x1, x2, x3, x4, x5, x6, x7]
            if isValid(x):
                x.append(f(x))
                popg.append(x)

    return popg


print(f([1, 2, 3, 4, 5]))

popg = generare(5)
