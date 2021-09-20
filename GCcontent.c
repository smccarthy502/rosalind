/* author: Sarah McCarthy
   date created: 9/15/2021
   takes in 10 DNA strings in FASTA format and returns ID and GC content of string with highest GC content
*/

#include <stdio.h>

int main(void){
    FILE *fp = fopen("rosalind_gc.txt", "r");
    char buff[255];
    
    fscanf(fp, "%s", buff);
    printf("%s", buff);

    /*
    char DNA[1032] = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT";

    int GC_count = 0;
    int nucleotide_count = 0;
    for(int i = 0; i < 1032 && DNA[i] != '\0'; i++){
        if(DNA[i] == 'G' || DNA[i] == 'C'){
            GC_count++;
        }
        nucleotide_count++;
    }

    float GC_content = (float)GC_count / nucleotide_count;
    printf("%f\n", GC_content);
*/
    fclose(fp);

    return 0;
}