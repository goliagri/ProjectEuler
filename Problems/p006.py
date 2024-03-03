import math 
import numpy as np

def p006(n):
    '''
    Problem description:
    Find difference between sum of squares and sqaure of sums of first n natural numbers
    '''
    
    sum_of_squares = 0
    for i in range(1,n+1):
        sum_of_squares += i**2
    
    square_of_sum = ((n+1)*n/2)**2
    return int(square_of_sum - sum_of_squares)

def tests():
    print(p006(100))

def main():
    tests()


if __name__ == '__main__':
    main()

