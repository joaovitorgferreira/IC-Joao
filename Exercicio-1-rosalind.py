dna = open("rosalind_dna.txt",'r')
countA = 0
countC = 0
countG = 0
countT = 0
for text in dna:
    for letter in text:
         if letter is 'A':
           countA = countA+1
         elif letter is 'C':
            countC = countC+1
         elif letter is 'G':
            countG = countG+1
         elif letter is 'T':
            countT = countT+1
print(countA,countC,countG,countT)