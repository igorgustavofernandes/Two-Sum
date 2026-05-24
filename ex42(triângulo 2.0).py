l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode ser um triângulo')
    if l1 == l2 and l2 == l3:
        print('Por ter três lados iguais, esse seria um triângulo do tipo Equilatero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Por ter dois lados iguais, esse seria um triângulo do tipo Isóceles')
    else:
        print('Por não ter nenhum lado igual, esse seria um triângulo do tipo Escaleno')
else:
    print('Não pode ser nenhum tipo triângulo')