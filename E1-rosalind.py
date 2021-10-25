#Método 1
print("Método 1")
dna = open("rosalind_dna.txt",'r')
countA = countC = countG = countT = 0 # Um modo prático de atribuir o mesmo valor à diferentes variáveis. Evita mais linhas de código 
for text in dna:
   for letter in text:
      if letter == 'A': # procure usar == para comparar valores
         countA += 1 # quando vamos somar um novo valor ao valor atual de uma varial podemos usar +=. O mesmo vale para outros operadores
      elif letter == 'C':
         countC += 1
      elif letter == 'G':
         countG += 1
      elif letter == 'T':
         countT += 1
print(countA,countC,countG,countT)

# Método 2 menos loops
print("Método 2")
dna = open("rosalind_dna.txt",'r').readline() #usando o método readline vc já consegue acesso direto ao conteúdo do arquivo. Isso corta um loop
countA = countC = countG = countT = 0
for nucleotide in dna:
   if nucleotide == 'A':
      countA += 1
   elif nucleotide == 'C':
      countC += 1
   elif nucleotide == 'G':
      countG += 1
   elif nucleotide == 'T':
      countT += 1
print(countA,countC,countG,countT)

# Método 3 sem loops
print("Método 3")
dna = open("rosalind_dna.txt",'r').readline()
dna_list = list(dna) #Um vez que vc tem acesso ao conteúdo do txt dá pra transformá-lo numa lista
A = dna_list.count("A") #Listas tem muuuuitos métodos úteis. Esse conta o núméro de ocorrencias de um valor.
C = dna_list.count("C")
G = dna_list.count("G")
T = dna_list.count("T")
print(A,C,G,T)
