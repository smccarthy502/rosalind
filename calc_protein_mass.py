# author: Sarah McCarthy 
# date created: 9/20/2021
# given a string of amino acids, calculate the weight using a monoisotopic mass table
# rosalind PRTM

import sys

#dictionary for finding weights of each amino acid
monoisotopic_mass_table = { 'A':71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259, 
                            'F':147.06841, 'G':57.02146, 'H':137.05891,'I':113.08406, 
                            'K':128.09496, 'L':113.08406, 'M':131.04049, 'N':114.04293, 
                            'P':97.05276, 'Q':128.05858, 'R':156.10111, 'S':87.03203,
                            'T':101.04768, 'V':99.06841, 'W':186.07931, 'Y':163.06333 }

#error checking to make sure we get 1 and only 1 input argument 
if len(sys.argv) !=2:
    sys.exit('missing or too many arguments (expecting only one input string)')

#get the input string from the argument list
input_string = sys.argv[1]

#total weight keeps track of total weight of the protein
total_weight=0

#go through string and add weight of each amino acid 
for amino_acid in input_string:
    amino_acid_weight = monoisotopic_mass_table[amino_acid]
    total_weight += amino_acid_weight

#print the result 
print('\n')
print(total_weight)