frase = []
def escreva(txt):
    print('-'*30)
    print(txt)
    print('-'*30)



for c in range(0,3):
    frase.append(str(input('Digite um texto: ')))
for frases in frase:
    escreva(frases)
