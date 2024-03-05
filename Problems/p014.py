import math 
import numpy as np

def p014(n):
    '''
    Problem description:
    Find the starting number under n million with the longest Collatz chain
    '''
    known_chain_lengths = {}
    max_val = 0
    max_num = -1
    for i in range(1,n):
        if i in known_chain_lengths:
            continue
        val = float(i)
        itr = 1
        seen = [val]
        while val != 1:
            if val % 2 == 0:
                val /= 2
            else:
                val = 3*val + 1
            
            if val in known_chain_lengths:
                itr += known_chain_lengths[val]
                break
            
            seen.append(val)
            itr += 1

        if itr > max_val:
            max_val = itr
            max_num = i
        
        for i,x in enumerate(seen):
            known_chain_lengths[x] = itr - i
        
    return max_num
            

def tests():
    print(p014(int(1e6)))

def main():
    tests()


if __name__ == '__main__':
    main()

