#author: Sarah McCarthy 
#date created: 9/13/2021
#takes in 10 DNA strings in FASTA format and returns ID and GC content of string with highest GC content
#rosalind GC

in_DNA = '''>Rosalind_6674
CTAAGTAGTAATCACGTGGGCATTAATGCCTTAGCGGAGGTTATACTTCCGTTTACATTG
CGCCCCTTTAATCCCTGGTCGGGTCAATGGTCTTAGTAGGTACAGGACCGGTACGATTGG
GGAGGCGGAGTCAGGAGCAAGTCGGGTACTTAGTTATTGAATCTGGCGGATACCGAAACA
TACCATTCAATTCATATTGTAAGACCAGCCTTACCTATTAAGTCATAGATAGAGCTTGAG
AATCTCCGTTCAAAAGCTGGTAGTGATTGTCTCCGGCTGACGTTGATCAGCAACGCCCAA
AGCCGTGTCAATAGTGGCATCTACGATGTCACGTGCTGGTGGAACGTCTAGATTATTCAT
TATAGCGTTGAGGTTATAGCTCCCGACGGAGGTCTCACGTACCACCTAATCCTATTACCT
TGACCAATAGATTTAACCAAAGCTCACGCGAGCTCGCTATACATGATAGGCCGCCCCCTC
GACCTCTGGGTTTGCAATCTTGTTCTCGATATGAGTTCGTTTGCAAGAGGGTTGGAGGAG
GCTACTTCGCAAAGAAGAACGCGTCAAATATCCCGCAGTTACCAACCGGCGAGGTTTGGA
CAGTCTGCCGCGCTGATCGGCTAGATCGTTGCACCTCAAGTAACATGGCGGGCCACGAAA
TTTGTCGTATACCATGTCCGGAGCCGAGCACTTAAAATGGCGCAACCTATTACGAACATG
CAGTGCAGCCTTGTTATCGACATACCCGGCTATCTCACCCGCGCTGTGTACGTTTTTGTT
CTATTAAGCTCGTTCGCTATACTTCCGTTTATTATCAAAGTAGCAGTAGCAAAGACGGGG
TCCTCGTGATAGAGCCTCCCGGGTACAATATAAACGATTTTCTGTAGGTATTGGCATTTC
GATTCCAAAATTCGTGTAGGAGTCCAGATTAGCAAGCTCGCCGGGTACAAGTAAACCTCA
GTGGCACGTATATAAATTGGAAAGG
>Rosalind_3857
GAGAGCGCGGAGAGACAATTGTGTCCCCAGCCCCTACGTTACGAGTACGATTGGCGACCA
GCTAGACCTACTGTTAGCAGATCTGGTGGGTGCCGAGTTACCAGTGGGTATCTGATTCGG
ACTAAGGGTGCTGAACGTGATCAAGGATTTTATTAATCAGAGTAGACACACTTATGTCGT
CAAGTGGGGGAACGCATGCCCCTAGTAGGCGTGATGCGGTGCTGCCAGCGTCCCCGAAAC
GGGAAAGCGTGGTTGACACTTTCTAGGGATACGACAAGTACGTAGACGAATATCTTGCCC
CGTAGACATCTCAACGAGTGACATGACCTAGTTATGGCATTAAGTTCCCGTGTACTCATT
CTCAGGGCAAATAATGGTAACCGGTGCACGAACTGAGTTTCTCCTCTATCTCATTTGTCC
AATTTATTCGAGGAGGTCTCTGCTGATCCCCGTCGTCGTCCGCGGCGTATAATAGGCAAA
GTGAAATGGTTATCGATTTCCGGGGGGGGCTCAACCATTGGTCTTGTTAAGGGCCTGCAA
TCCACAAATTAATTATGTATACGTGGGACGTGGCTGTGTGCCGCGTGGTTCAACATATCG
AATTATCTAAAATTTGATATTACCAGTTAGCATACAAGCGGTTTAATCGTGTATACCGTA
CCTTACACCAAAGGCTTAAATTCTCGGGTTTACAGTACCGATCATTATCTCCCTTCCATG
CTTCTGCTACCTAGCATTTTGCGCCAAGATGTTTGTATGCCCTTTGGTAATGGCAGGAAA
AGGGTTCAGGTCAGACAGAAACTATGTTGAGAGACTGTGTAAGTATAATAATCATGGTGA
GCCAAATGAGCTCCCGATGACGCGGCCGGGGAGATTTACAATCTAACCGCTGAATTAGTG
GCTGGAACATGCCACTCCCATGCGGTGCCCCGAACACAGGAATGGCGAACCCATGCATGT
GGCTTGTCGGAACCTTGT
>Rosalind_2345
GCCCTCGCGAAGCTTTGTCGGGTCTGGTAAGTTGACCGCCATTCTCGAGTCATGTTCTTA
TCGGACGTCTATGTGCTGGAATCCAGTCCGCACTAGACCGAGTAGAAGGCTAGCTCATGA
AAGTCGATCTTGTCGACTGGTGTACGATTCGAGCTGTATACATACATTAAACATTTTCAT
CACGACTTTGTAGCTGGGAGAACAGGGGATTCATCCGGGACTCTCCAATCAGGGCCACTG
AACTCGCTCGATATCAAGTTGACATTGAGATGATAGACGTCGGCACGTATTTCCTGTAAC
AAATCACGCGACTTAGGGCATCGGGGACTCGAAACTGAATATGTCGTCTTAGCCCCCTCT
TGACGAGGTGCGGGTGGTGGTGTAACTAGACTCTTTCCGTCGCTACCCTCAAACAGGGCG
GACGTGTCGTACATGCAGATGAGAGGATGGTCTCGCACTCGTGCTAGCGGCTGGTGCTTC
CTTCAACTTGGACACCGACCACGTTGGATGTGAGCGATCACCCGTTCCCGAAAGCTTTCT
ACTTGTGGTGTCTTGGTAGATAAGAGCTTGACGAGTGAGGTTCTACTGTACGACGAGGGA
ATCTGTATCGGACGCAATCCGAGACAATCACAGCGTGTGTGGCTCGTTGCCGTCGGTTCC
TAAAAGTCAGCACACACATGTTTACAATGCCAGGACCAGAGGGGTAGCATTACTTCGTAT
GGTGCGCGCCACACGACGCCTATACCAGGGAGATGGCCCTGATGGTTAGCTCCAAGTCAT
GGCAATATCCATACCGATACCGTCCAGGGAAGCCGTTGAGCAAAGAAGGGAGGCCGTCCA
GCTTCCTGCTACCGACAGAAGATAGGAGTCGGCTCATCGTTTAGCCCCCAGTGAGGCAGG
AAGACATGTCCAACGGGGGACTGCCTAGCTCCTCCCC
>Rosalind_5663
ACGGCTGTCCCTATGCTAATGCCTGTGTAAGTAGGAACTAGGTGGCAGTGACCGACTCCC
TACGTCAAGTTCTGAGGGCTCTTAATCAAAGTTCTGCTAACGCAGTGTATTGACTTGCCT
TACCGAAAGACTGGGGACCCGACGCTCCTTACACACATTTAGAAGTCACGTCTTGCTGCT
CATATGGCCCTTCGACATTGCGCTCTCATATATAGATTGCCTGTGTAGTATAATTAGACT
TTCTCGCATAGATAGATGAAGACGGGCCCCACTGGTAGACCCTTGACCAGCACTTGTACT
GAGCACATCTGTTTCAATGACTTAGGAGTAGGTCGAAGGACGTCTATTCCCAGCAGTTGC
ACGTATTCGAACCTCTGAAGCGTCCACCTGTGCTTATGGGTACTAGCGCAAGGCAGGGCA
ATATCGCTGTGCATCTAAGGACGGACGCGTTGTCTTGGATACCACTGCTTGTTAAGCGGT
AAGAGGTCACCGGGAACGCATCAAAGGGAAAATTTTTTCCACAGACATTGGAAGCGTAGT
TGATTCGTTGCCCTACTTGTAGGGATTTCCTATAGCTTTTGGCAGCCGCACATGTGAGGC
TGTCTCCTCCTACAGGCATCATACCCGTGGTGCAGCTCCGGAGTTGGTCCGTACGGACCC
GCAAGCCGTGTGTGCATGGCGATATATAACCCGTTACCATGCGAACCAATCAATCTCTAT
TGGATGGATCAGGAATAATGCAACCGACAATGGATGAGCTTTCTCCGCGCGCAAGAAGAA
AAGCAGTATATAATCATACTGAATTTCGGGCATCCCAGGGCAGCGTAGGGTGGCGCTGAA
TGTACCATCTTAATTACACGTTCATCCGGGTAGCGTACAAGCGTGAGTTCTGATCAATCA
CCTGCTGACGTCATG
>Rosalind_0796
CTTCAACCATGGAAAGCTTTCGCCGCGTTCTCCAAGCGGTCGATCGGATCACTCATGCCA
GTTCACCGGCTGAGACGTATTAATGGAAACGTCGCCTACCGGGCCCTGTAGATGTAAAGT
TACCCCCATTATGCGCCGCCCATCGTTCTTTCCCAGTAAGCCCCGATGATTTTCGGGATC
GCCCCATTTGGATGTATTGGCCGTTCTTTCTAGTCGTGGATTCGATGTTGTTCCTTTTGG
CTCACGCCTAAAATAAGTCTGCGATTCAATAGCGGGAGACCACGTGTCACTCCTCGTCTG
CGGACGCACGGATAAGCGTTGACCCCTTTCCGCCGGGCCTCACCGCTGTACGATTCAGTT
GACCCGTTTTGCCGTTCGAATGTTCCCGCACTTTGCGCAGTGAAATACAGAACACAGTCA
CCTTTAGGACACCGACATTTCGACGCTAGTCAGGGCCATGGACCTTATCTAGCTTGTGGT
GAACTTAGAAGTGATACCAATCCAATGGGTTGATAGATGTTAGACCTTGCGTGATGTTAT
TCGCATACACATTGCCTGACCCGGGTCCCATAACTCTGGATAATACAAACATGAGGTGGG
GACCTCGGGAACGCTGAGCAGACGCTCGGAATCGTATTCTGTGTTATCCATCGCCTTTCG
GTATTGCGTTGCTACAAGGTCGAAGACGCGCAACCGTGACCCGTCGATTGTTCCCTAGAC
TAAACCTTCTTACATACGGACCAGGGCGCGCAATTAAGAGGCGAGACATTGAGGATACCG
CTGAATGTGCGGGAATATTGGCTAATATGGTAGTCCTATGTTAGTTTACCGGAACAACCT
ACCCGTTACGGGGAGTCCTAGCTCAT
'''

#print(ID)
curr_ID = ''
curr_DNA = ''
curr_GC = 0
curr_GC_content = 0
curr_count = 0
max_GC = 0.0
max_GC_ID = ''
in_DNA_list = in_DNA.split()
for line in in_DNA_list:
    if line[0] == '>':
        if curr_count > 0:
            curr_GC_content = curr_GC / curr_count
            if curr_GC_content > max_GC:
                max_GC = curr_GC_content
                max_GC_ID = curr_ID
        curr_ID = line
        curr_GC = 0
        curr_count = 0
    else:
        curr_DNA = line
        for i in range(len(curr_DNA)):
            if curr_DNA[i] == 'G' or curr_DNA[i] == 'C':
                curr_GC += 1
            curr_count +=1

curr_GC_content = curr_GC / curr_count
if curr_GC_content > max_GC:
    max_GC = curr_GC_content
    max_GC_ID = curr_ID

print(max_GC_ID[1:])
print(max_GC*100)
