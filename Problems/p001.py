import math 

def p001(x1, x2, max_val=1000): #max is not inclusive
    '''
    Get sum of integers (0,max_val) which are divisible by either x1 or x2
    '''
    x_lcm = math.lcm(x1, x2)

    def get_seq_sum(factor, max_):
        seq_len = (max_-1) // factor
        return factor * ((seq_len+1) * seq_len)//2 
    
    return get_seq_sum(x1, max_val) + get_seq_sum(x2, max_val) - get_seq_sum(x_lcm, max_val)

def tests():
    print(p001(3,5,1000))

def main():
    tests()


if __name__ == '__main__':
    main()

