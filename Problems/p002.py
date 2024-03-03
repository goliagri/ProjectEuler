import math 
import numpy as np

def p002(max_val): #max is inclusive
    X = np.ones((2,1))
    X[0][0] += 1
    transform = np.array([[1,1],[1,0]])
    res = 0
    while X[0][0] <= max_val:
        if X[0][0] % 2 == 0:
            res += X[0][0]
        X = np.matmul(transform, X)
    return int(res)


def tests():
    print(p002(4e6))

def main():
    tests()


if __name__ == '__main__':
    main()

