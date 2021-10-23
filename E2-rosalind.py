dna = open("rosalind_rna.txt", 'r')
text = dna.read()
resposta = text.replace("T", "U")
print(resposta)