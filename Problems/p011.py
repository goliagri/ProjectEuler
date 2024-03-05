import math 
import numpy as np

def pxxx(grid, k):
    '''
    Problem description:
    Get the largest product of k adjacent numbers in any direction in a straight line in grid
    '''
    n, m  = np.shape(grid)
    max_val = 0
    #vertical strips
    for i in range(n-(k-1)):
        for j in range(m):
            prod = np.prod(grid[i:i+k,j])
            max_val = max(max_val, prod)
    
    #horizontal strips
    for j in range(m-(k-1)):
        for i in range(n):
            prod = np.prod(grid[i,j:j+k])
            max_val = max(max_val, prod)

    #lr diagonal strips
    for i in range(n-(k-1)):
        for j in range(m-(k-1)):
            prod = np.prod(np.diagonal(grid[i:i+k, j:j+k]))
            max_val = max(max_val, prod)
    
    for i in range(k-1, n):
        for j in range(m - (k-1)):
            prod = np.prod(np.diagonal(np.fliplr(grid[i-(k-1):i+1,j:j+k])))
            max_val = max(max_val, prod)
        
    return max_val

def tests():
    file = open("data/p011_input.txt", "r")
    lines = file.readlines()
    file.close()
    grid = [line.strip().split(' ') for line in lines]
    grid = [[int(x) for x in line] for line in grid]
    np_grid = np.array(grid)
    print(pxxx(np_grid, 4))

def main():
    tests()


if __name__ == '__main__':
    main()

