from time import sleep

def linha():
    print('-'*30)
def contador(inicio, fim, caminho):
    print(f' Contagem de {inicio} até {fim} de {caminho} em {caminho}')
    if caminho < 0:
        caminho *= -caminho
    if caminho == 0:
        caminho += 1
    if inicio < fim:
        cont = 1
        while cont <= fim:
            print(cont, end=' ', flush=True)
            cont += 1
            sleep(0.5)
        print('FIM')
    else:
        cont = 10
        while cont >= fim:
            print(cont, end=' ', flush=True)
            cont -= 1
            sleep(0.5)
        print('FIM')

linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é sua vez!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
caminho = int(input('Caminho: '))
contador(inicio, fim, caminho)
