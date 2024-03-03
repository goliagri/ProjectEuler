import math 

def p004(digits):
    '''
    Largest palindrome made from numbers with <digits> digits
    '''
    def is_palindrome(x):
        str_x = str(x)
        for i in range(0, len(str_x)//2):
            if str_x[i] != str_x[-i-1]:
                return False
        return True
    
    max_val = 0
    for i in range(10**(digits-1), 10**digits):
        for j in range(i, 10**digits):
            if is_palindrome(i*j):
                max_val = max(max_val, i*j)
    return max_val

def tests():
    print(p004(3))

def main():
    tests()


if __name__ == '__main__':
    main()

