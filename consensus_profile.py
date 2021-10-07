# author: Sarah McCarthy 
# date created: 10/05/2021
# given a collection of DNA strings in FASTA format, return a consensus string and profile matrix
# rosalind 

import sys

infile = sys.argv[1]
f = open(infile, 'r')
DNA_strings = f.read()
f.close()

count = 0
for line in DNA_strings.splitlines():
    if line[0] == '>' and count == 0:
        continue
    elif line[0] == '>':
        break
    else:
        count = count + len(line)

print(count)
        
profile_a = 