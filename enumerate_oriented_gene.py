# author: Sarah McCarthy
# date created: 10/07/2021
# given positive integer ,+6, return total number of signed permutations and list of all permutations 
# rosalind SIGN

import sys
from itertools import product 
n = int(sys.argv[1])

permutations = list(product(*((x, -x) for x in range(1,n+1))))

print(permutations)