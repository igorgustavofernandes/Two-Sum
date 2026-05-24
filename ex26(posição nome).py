frase = str(input('Digite uma frase: ')).upper().strip()
print ('Essa frase tem {} vezes a letra "a"'.format(frase.count('A')))
print ('O primeiro "A" está na posição {}'.format(frase.find('A')+1))
print ('O último "A" está na posição {}'.format(frase.rfind('A')+1))