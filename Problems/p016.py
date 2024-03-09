import math 
import numpy as np

def p016(params):
    '''
    Problem description:

    '''
    return sum([int(i) for i in str(2**params)])

def tests():
    print(p016(10000))

def main():
    tests()


#if __name__ == '__main__':
#    main()

def sum_of_digits(n):
  """
  Calculates the sum of the digits of 2^n.

  Args:
    n: An integer representing the exponent of 2.

  Returns:
    The sum of the digits of 2^n.
  """
  result = 2**n  # Calculate 2^n
  total_sum = 0
  while result > 0:
    total_sum += result % 10  # Add the last digit to the sum
    result //= 10  # Remove the last digit 
  return total_sum

# Example usage
n = 15
result = sum_of_digits(n)
print(f"The sum of the digits of 2^{n} ({2**n}) is {result}")