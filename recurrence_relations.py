#author: Sarah McCarthy 
#date created: 9/13/2021
#takes in n and k and returns number of rabbit pairs after n months presuming each mature rabbit pair produces k rabbit pairs 
#rosalind FIB

#number of months (<= 40)
n = 35
#rabbit pairs produced by each mature pair 
k = 4

#start with 1 immature pair, won mature pair
immature  = 1
mature = 0

#for loop for the number of months 
for x in range(n-1):
    tmp = k * mature 
    mature = mature + immature
    immature = tmp

#calculates the number of pairs 
total = immature + mature
print(total)