classificacao = 'Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Athletico-PR', 'Bahia', 'Bragantino', 'Vasco da Gama', 'Coritiba', 'EC Vitória', 'Cruzeiro', 'Botafogo', 'Atlético-MG', 'Internacional', 'Santos', 'Corinthians', 'Grêmio', 'Mirassol', 'Remo', 'Chapecoense'
print('-=' * 20)
print('Brasileirão - Tabela')
print('-=' * 20)
print('G4 =', *classificacao[0:4])
print('Z4 =', *classificacao[16:20])
print('A-Z =', *sorted(classificacao))
print(f'Chapecoense está em {classificacao.index("Chapecoense")} lugar.')