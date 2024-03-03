import math 
import numpy as np

def p007(n):
    '''
    Problem description:
    Get the nth prime number
    '''


    def is_prime(i):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                return False
        return True
    
    prime_count = 0
    i = 1

    while prime_count < n:
        i += 1
        if is_prime(i):
            prime_count += 1
    return i

def tests():
    print(p007(10001))

def main():
    tests()


if __name__ == '__main__':
    main()

