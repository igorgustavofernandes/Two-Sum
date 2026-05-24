pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['média'] = float(input(f'A média de {pessoa["nome"]}: '))
if pessoa['média'] >= 7:
    pessoa['status'] = 'Aprovado'
else:
    pessoa['status'] = 'Reprovado'
print('-='*10)
print(f'O nome é igual a {pessoa["nome"]}.')
print(f'A média é igual a {pessoa["média"]}')
print(f'Status é igual a {pessoa["status"]}')
