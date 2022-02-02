# author: Sarah McCarthy
# date created: 02/01/2022
# given two integers k and N, return probability that at least N AaBb organisms will belong ot k-th generation  
# rosalind LIA

import math

#given variables 
k = 5
N = 9

#calculate the end of the range for the sum
P = 1
for i in range(k):
    P = P * 2

tot_probability = 0
for i in range(N, P):
    prob = (math.factorial(P)/(math.factorial(P-i)*math.factorial(i)))*pow(0.25,i)*pow(0.75,P-i)
    tot_probability += prob

print(tot_probability)


