import math 

def p003(num):#max is not inclusive
    '''
    Get largest prime factor of num
    '''
    prime_factors = {}
    for i in range(2, int(math.sqrt(num))+1):
        while num % i == 0:
            num = num // i 
            prime_factors[i] = 1 + prime_factors.get(i, 0)
            if i**2 > num:
                prime_factors[num] = 1
                break
    return max(prime_factors.keys())



def tests():
    print(p003(13195))
    print(p003(600851475143))

def main():
    tests()


if __name__ == '__main__':
    main()

