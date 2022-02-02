# author: Sarah McCarthy
# date created: 10/08/2021
# given a string, return the location and length of all reverse palindromes in the string 
# rosalind REVP

import sys

#get and open input file 
infile = sys.argv[1]
f = open(infile, 'r')
DNA_string = f.read()
f.close()

#input DNA string
DNA = ''

for line in DNA_string.splitlines():
    if line[0] == '>':
        continue
    else:
        DNA = DNA + line

#substrings used for comparison
sub_DNA = ''
DNA_palindrome = ''

restriction_sites = {}

#go through the input string and grab substrings of length i
for i in range(4,13):
    for j in range(len(DNA) - i+1):
        sub_DNA = DNA[j:j+i]
        DNA_palindrome = ''
        #build the palindrome 
        for k in range(i):
            if sub_DNA[k] == 'C':
                DNA_palindrome = 'G' + DNA_palindrome 
            elif sub_DNA[k] == 'G':
                DNA_palindrome = 'C' + DNA_palindrome 
            elif sub_DNA[k] == 'T':
                DNA_palindrome = 'A' + DNA_palindrome 
            else:
                DNA_palindrome = 'T' + DNA_palindrome 
        if sub_DNA == DNA_palindrome:
            #print(sub_DNA + ' ' + str(j+1) + ' ' + str(i))
            restriction_sites[j+1] = i

#print(list(restriction_sites))
for position in list(restriction_sites):
    print(str(position) + ' ' + str(restriction_sites[position]))