import math
an = float(input('Digite o ângulo: '))
se = math.sin(math.radians(an))
print('O SENO do ângulo {:.0f} é {:.2f}'.format(an, se))
co = math.cos(math.radians(an))
print('O COSSENO do ângulo {} é {:.2f}'.format(an, co))
tan = math.tan(math.radians(an))
print('o TANGENTE do ângulo {} é {:.2f}'.format(an, tan))