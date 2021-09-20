#author: Sarah McCarthy 
#date created: 9/13/2021
#converts DNA to RNA
# rosalind RNA

#input DNA string 
#in_DNA = 'GATGGAACTTGACTACGTAAATT'
in_DNA = 'GCGTTGGCTCTAACTGGGTTGCGTTACACGAGATTCACGCTAGACTTTCTTGACGGGAATTCTGCTACCGCGATGGAGTCCCGGTCAGTTTTGGCACCGATTTGCTGGGGTAGTGTGTAAGGATCCGGTTTCATCCACCTAACCTATCCAGATACTAGCGTCTAATTCTACAGCGTCCGAGAAAGCTCCTGTGGGTGTACAATTAGTTGTTTATCCGAAATACTAGCCTAGGGCATAATGTTCCTTCCTTTAAGCTTGTGGGTCACCCTATGCAAGCCTTCTTCCGATGAACCGCGACCTCTCCGCGAATACTTCCGCTCCCTGAGGGCTCTATGAAGTGGTTAGTCCTATCGACGGCCGGGTGGGTGAACGCTCACTGGACATGAGATGGTTTATCTAGGATCAATTCAACGAAGGTTCCACTGCCTTGTGGTCCTTATGTCGATAACATCCTATCCTGACCCGGATCTCATGCGTCTCTAGCACTATCACCCTGGACGGCCGTCCTTGGCTCACGGCGAAAGCCTTTTGTTACAACGATATGCGACGTTTAAACGAACTTGCTTGCTGGGGGTCCGCCGTCGTGTGCACCAAGCTTGCCCGAAGGCTTGCTACCGGGGGTCGATTGAGACTAAACTTTCATGCGGTAGAGAATACGTTTTCTAGAGATGCTGCGCTGAACTGACAGTGGCGGAGTGCGTCACGCCGCTAGCAGTCTATACTCTGTCGTATCACGGACCTACCAAGGATATAGGCTTCACTTTGTAACTCCAGGGGGAGCGAGGGTGTTAACACGAAATTTCCAACATGAATGAGATGGTATATATTCTTCAGTGCATCGTACTTGCCGTTGAACTACTCTCCGGCGCGATCCTCGATACTGTGACACTTACTGAGAACACGGCTCTCCTAAAGCTC'
#string for output 
out_RNA = ''

#go through input DNA string
#assign nucloetide to RNA string based on DNA base 
for nucleotide in in_DNA:
    if nucleotide == 'A':
        out_RNA = out_RNA + 'A'
    elif nucleotide == 'C':
        out_RNA = out_RNA + 'C'
    elif nucleotide == 'G':
        out_RNA = out_RNA + 'G'
    elif nucleotide == 'T':
        out_RNA = out_RNA + 'U'
    else:
        print('error not a valid nucleotide input')

#print out the answer 
print(out_RNA)