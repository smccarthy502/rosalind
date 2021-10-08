# author: Sarah McCarthy 
# date created: 10/07/2021
# given DNA string and collection of substrings acting as introns, return protein string from trasncribing and translating exons of DNA string 
# rosalind SPLC

import sys

###############################################################################################

#function for converting RNA string to protein string 
def RNA_to_protein(RNA):
    table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
    }

    peptide = ""
    aminoAcid = ''
    i = 0

    while i < len(RNA):
        aminoAcid = table[RNA[i:i+3]] #look up the amino acid in the dictionary
        if aminoAcid == 'STOP': #reached end of translation
            break
        peptide = peptide + aminoAcid #add the amino acid to the peptide string
        i += 3

    return peptide

########################################################################################################

#function to convert DNA string to RNA string
def DNA_to_RNA(DNA):
    #string for output
    RNA = ''

    #go through input DNA string
    #assign nucloetide to RNA string based on DNA base 
    for nucleotide in DNA:
        if nucleotide == 'A':
            RNA = RNA + 'A'
        elif nucleotide == 'C':
            RNA = RNA + 'C'
        elif nucleotide == 'G':
            RNA = RNA + 'G'
        elif nucleotide == 'T':
            RNA = RNA + 'U'
        else:
            print('error not a valid nucleotide input')

    #return the answer 
    return RNA

###########################################################################################################

#get and open input file 
infile = sys.argv[1]
f = open(infile, 'r')
DNA_strings = f.read()
f.close()

# s is the input DNA string 
s=''
# curr_intron is used to build the intron 
curr_intron = ''
# list for all introns to remove from s
introns_list = []
# boolean to keep track of whether we have completed input string concatenation 
s_completed = 0
for line in DNA_strings.splitlines():
    if line[0] == '>' and not s:
        continue
    # done gettign lines for input s, move on to getting introns 
    elif line[0] == '>' and s and not curr_intron:
        s_completed = 1
    # reached the end of one intron and start a new intron 
    elif line[0] == '>' and curr_intron:
        introns_list.append(curr_intron)
        curr_intron = ''
    # concatenate the input string together 
    elif s_completed == 0:
        s = s + line
    # concatenate the intron
    else:
        curr_intron = curr_intron + line
    
# add the last intron to the list of introns
introns_list.append(curr_intron)

exon = s

# delete introns from the input strings
for introns in introns_list:
    exon = exon.replace(introns, '')

# convert final DNA string to RNA
RNA = DNA_to_RNA(exon)

#convert RNA to protein
protein = RNA_to_protein(RNA)
print(protein)
