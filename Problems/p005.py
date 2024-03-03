import math 
import numpy as np

def p005(n):
    '''
    Problem description:
    Get the smallest positive number divisible by all integers [1,n]
    '''
    def prime_factors(x):
        prime_facs = {}
        for j in range(2,int(math.sqrt(x))+2):
            if x == 1:
                break
            while x % j == 0:
                x /= j 
                prime_facs[j] = 1 + prime_facs.get(j,0)
            if x < j**2 and x != 1:
                prime_facs[x] = 1 + prime_facs.get(x,0)
                break
        return prime_facs

    primes = {}
    for i in range(2,n+1):
        i_primes = prime_factors(i)
        for key, val in i_primes.items():
            primes[key] = max(primes.get(key, 0), val)
    
    return int(math.prod([key**val for key, val in primes.items()]))


def tests():
    print(p005(20))


def main():
    tests()


if __name__ == '__main__':
    main()