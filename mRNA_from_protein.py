# author: Sarah McCarthy
# date created: 9/20/2021
# given protein string, return number of different RNA strings from which the protein could have been translated 
# rosalind 

import sys

#dict for number of RNA strings that can code for each amino acid
amino_acid_RNA = {  'M':1, 'T':4, 'N':2, 'K':2, 'S':6,
                    'R':6, 'V':4, 'A':4, 'D':2, 'E':2,
                    'G':4, 'F':2, 'L':6, 'Y':2, 'C':2,
                    'W':1, 'P':4, 'H':2, 'Q':2, 'I':3}

#input protein string
protein_string = sys.argv[1]

#used to keep track of the RNA strings that could make the protein
number_of_RNA_strings = 1

#go through protein string char by char
#look up numbr of RNA strings for amino acid
#multiply to get number of possible strings 
for amino_acid in protein_string:
    curr_amino_acid_num = amino_acid_RNA[amino_acid]
    number_of_RNA_strings = (number_of_RNA_strings *curr_amino_acid_num) % 1000000

#multiply by 3 for the STOP
number_of_RNA_strings = (number_of_RNA_strings *3) % 1000000
print(number_of_RNA_strings)