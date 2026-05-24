altura = float(input('Qual a altura em metros: '))
largura = float(input('Qual a larguara em metros: '))
area_total = altura * largura
lata = 2
quantidade = area_total / lata

print ('A dimensão da parede é {}x{} e sua area total é {}m².'.format(altura, largura, area_total))
print ('Você precisará  {:.1f}l de tinta'.format(lata))