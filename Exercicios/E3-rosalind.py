dna = open('rosalind_revc.txt','r')
text = dna.read()
#metodo string[::-1] inverte a ordem de string
rev_text = text[::-1]
#metodo para traduzir multiplas letras num string
transTable = rev_text.maketrans("ATCG", "TAGC")
resposta = rev_text.translate(transTable)
print(resposta)