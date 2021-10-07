# author: Sarah McCarthy 
# date created: 10/05/2021
# returns total number of permutations of length n and list of all such permutations
# rosalind PERM

import sys
from itertools import permutations
import re

#get number of permuations to do
n = int(sys.argv[1])
num_permuations = 1

#total number of permuations is n!
for i in range(1, n+1):
    num_permuations = num_permuations * i

#get the right permuation for the input number 
if n == 1:
    perm = permutations([1])
elif n == 2:
    perm = permutations([1,2])
elif n == 3:
    perm = permutations([1,2,3])
elif n == 4:
    perm = permutations([1,2,3,4])
elif n == 5:
    perm = permutations([1,2,3,4,5])
elif n == 6:
    perm = permutations([1,2,3,4,5,6])
elif n == 7:
    perm = permutations([1,2,3,4,5,6,7])
else:
    print("error number must be 1 - 7")
    exit()

#print result
print(num_permuations)
for i in list(perm):
    i = re.sub(r'[()]','', str(i))
    i = re.sub(r'[,]','',i)
    print(i)