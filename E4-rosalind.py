data = open('rosalind_fib.txt','r').readline()
lista = list(data)
print(lista)

k = int(lista[2])
n = int(lista[0])
sequencia_pop = [0,1] #inicia a sequência desde o mês 1
indice = 1

for pop in sequencia_pop:
    if len(sequencia_pop)<= n:
        sequencia_pop.append(sequencia_pop[indice-1]*k+(sequencia_pop[indice]))
        indice = indice + 1
print(sequencia_pop)






