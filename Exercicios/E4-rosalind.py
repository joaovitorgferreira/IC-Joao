data = open('rosalind_fib.txt','r').readline()
lista = list(data)
elemento1 = str(lista[0])+str(lista[1])

k = int(lista[3])
n = int(elemento1)
sequencia_pop = [0,1]
indice = 1

for pop in sequencia_pop:
    if len(sequencia_pop)<= n:
        sequencia_pop.append(sequencia_pop[indice-1]*k+(sequencia_pop[indice]))
        indice = indice + 1
print(indice)






