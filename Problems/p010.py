import math 
import numpy as np

def p010(n):
    '''
    Problem description:
    Get the sum of primes with values bellow n
    '''
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2,math.floor(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True
    
    res = 0
    i = 2
    while i < n:
        if is_prime(i):
            res += i
        i += 1
    return res

def tests():
    print(p010(2e6))

def main():
    tests()


if __name__ == '__main__':
    main()

