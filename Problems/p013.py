import math 
import numpy as np

def p013(nums):
    '''
    Problem description:
    Find first 10 digits of sum of nums
    '''
    nums = [float(num) for num in nums]
    res = sum(nums)
    return res // 10**(math.ceil(math.log(res, 10)) - 10)
    

def tests():
    file = open("data/p013_input.txt", "r")
    lines = file.readlines()
    file.close()
    nums = [line.strip() for line in lines]
    print(p013(nums))

def main():
    tests()


if __name__ == '__main__':
    main()

