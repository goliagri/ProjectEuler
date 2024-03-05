import math 
import numpy as np

def p012(k):
    '''
    Problem description:
    Find the first triangle number with at least k divisors
    '''
    def divisor_count(x):
        divs = set([1,x])
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                divs.add(i)
                divs.add(x/i)
        return len(divs)
            


    def triangle(x):
        return (x+1)*x/2
    
    n = 1 
    while divisor_count(triangle(n)) <= k:
        n += 1
    
    return int(triangle(n))

    

def tests():
    print(p012(500))

def main():
    tests()


if __name__ == '__main__':
    main()

