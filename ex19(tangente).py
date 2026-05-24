import random
yourname = str(input('Digite o seu nome: '))
hername = str(input('Digite o nome da sua namorada: '))
lista = [yourname,hername]
alpha = random.choice(lista)
print('O ALPHA do relacionamento é o(a) {}'.format(alpha))