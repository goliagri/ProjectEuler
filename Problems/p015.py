import math 
import numpy as np

def p015(n):
    '''
    Problem description:
    How many was are there to get from top left to bottom right of n x n lattice with only downward or rightward steps
    '''
    return (math.comb(2*n,n))

    

def tests():
    print(p015(20))

def main():
    tests()


if __name__ == '__main__':
    main()

