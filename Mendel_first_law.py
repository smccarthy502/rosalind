# author: Sarah McCarthy 
# date created: 10/05/2021
# given k, m, n representing population k individuals homozygous dominant, m are heterozygous, n homozygous recessive, returns probabilty that two randomly selected mating organisms will produce individual possssing donimant allele
# rosalind IPRB 
# referenced http://saradoesbioinformatics.blogspot.com/2016/06/mendels-first-law.html


import sys

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

population = k + m + n

probability = ((4*(k*(k-1)+(2*k*m)+(2*k*n)+(m*n))) + 3*m*(m-1)) / (4*population*(population-1))
print(probability)