# author: Sarah McCarthy 
# date created: 10/05/2021
# given a collection of DNA strings in FASTA format, return a consensus string and profile matrix
# rosalind 

import sys

#get and open input file 
infile = sys.argv[1]
f = open(infile, 'r')
DNA_strings = f.read()
f.close()

#figure out how many characters are in the DNA string 
count = 0
for line in DNA_strings.splitlines():
    if line[0] == '>' and count == 0:
        continue
    elif line[0] == '>':
        break
    else:
        count = count + len(line)

#arrays to keep track of the profile for each nucleotide 
profile_c = [0] * count
profile_g = [0] * count
profile_t = [0] * count        
profile_a = [0] * count

#if the line starts with > then it is the identifier line and not counted in the profile 
curr_position = 0
for line in DNA_strings.splitlines():
    if line[0] == '>':
        curr_position = 0
    else:
        #for through the characters and count for the profile
        for char in line:
            if char == 'C':
                profile_c[curr_position] += 1
            elif char == 'G':
                profile_g[curr_position] += 1
            elif char == 'T':
                profile_t[curr_position] += 1
            elif char == 'A':
                profile_a[curr_position] += 1
            else:
                print('not a valid character')
                exit()
            curr_position +=1

#build consensus string by finding the nucleotide with greatest count for each position 
consensus_string = ''
for i in range(count):
    if profile_c[i] >= profile_g[i] and profile_c[i] >= profile_t[i] and profile_c[i] >= profile_a[i]:
        consensus_string = consensus_string + 'C'
    elif profile_g[i] > profile_c[i] and profile_g[i] >= profile_t[i] and profile_g[i] >= profile_a[i]:
        consensus_string = consensus_string + 'G'
    elif profile_t[i] > profile_c[i] and profile_t[i] > profile_g[i] and profile_t[i] >= profile_a[i]:
        consensus_string = consensus_string + 'T'
    elif profile_a[i] > profile_c[i] and profile_a[i] > profile_g[i] and profile_a[i] > profile_t[i]:
        consensus_string = consensus_string + 'A'

#print result
print(consensus_string)

print('A: ', end='')
for element in profile_a:
    print(element, end=' ')
print()

print('C: ', end='')
for element in profile_c:
    print(element, end=' ')
print()

print('G: ', end='')
for element in profile_g:
    print(element, end=' ')
print()

print('T: ', end='')
for element in profile_t:
    print(element, end=' ')
print()