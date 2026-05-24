import random
print('--------------------------------------------')
print('Sorteio da melhor equipe de super hérois')
print('--------------------------------------------')
eq1 = str(input('Digite o nome da primeira equipe: '))
eq2 = str(input('Digite o nome da segunda equipe: '))
eq3 = str(input('Digite o nome da terceira equipe: '))
eq4 = str(input('Digite o nome da quarta equipe: '))
eq5 = str(input('Digite o nome da quinta equipe: '))
lista = [eq1, eq2, eq3, eq4, eq5]
random.shuffle(lista)
print('A melhor equipe de super herois em ordem decrescente (do melhor para o pior) é:')
print (lista)

