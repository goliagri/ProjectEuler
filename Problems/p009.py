import math 
import numpy as np

def p009(n):
    '''
    Problem description:
    Find a pythagorean triplet a**2 + b**2 = c**2 where a+b+c=n
    Returns None if no such pythagorean triplet exists
    '''
    for a in range(1,n):
        for b in range(a, n):
            c = math.sqrt(a**2 + b**2)
            if a + b + c > 1000:
                break
            elif a+b+c == 1000:
                return int(a*b*c)
    return None
            
    

def tests():
    print(p009(1000))

def main():
    tests()


if __name__ == '__main__':
    main()

