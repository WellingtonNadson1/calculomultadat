# Valor Base Bombeiro Militar
vbbm = 27.61

# Fator de Risco de Incêndio
fator_risco =  [1, 1.1, 1.2]

# Fator de Área Edificada
fator_area = [4, 8, 12, 16, 24, 30, 37, 43, 50, 56, 63, 69, 76, 83, 89, 94, 100 ]

# Definindo as listas de infrações primeiramente vazias
infra_leve = []
infra_media = []
infra_grave = []
infra_gravissima = []

# Seleção do Risco Contra Incêndio da Edificação a ser Multada
print('''
Escolha qual o fator de Risco da Edificação Multada:

0 - Risco Baixo (até 300 MJ/m²)
1 - Risco Médio (Entre 300 e 1.200 MJ/m²)
2 - Risco Alto (Acima de 1.200 MJ/m²)\n''')

# Pegando o valor digitado pelo usuário e utilizando como índice para 
# escolha do valor de risco da lista de fator de risco
risco = fator_risco[int(input('Qual o Fator de Risco da Edificação? '))]


# Apresentar a Seleção da Área da Edificação Vistoriada
print('''
Escolha o Tamanho da Área Edificada da Edificação a ser Multada:
0 - (até 200)
1 - (> 200 ≤ 500)
2 - (> 500 ≤ 750)
3 - (> 750 ≤ 1.500)
4 - (> 1.500 ≤ 2.500)
5 - (> 2.500 ≤ 3.500)
6 - (> 3.500 ≤ 5.000)
7 - (> 5.000 ≤ 7.000)
8 - (> 7.000 ≤ 10.000)
9 - (> 10.000 ≤ 20.000)
10 - (> 20.000 ≤ 30.000)
11 - (> 30.000 ≤ 40.000)
12 - (> 40.000 ≤ 50.000)
13 - (> 50.000 ≤ 60.000)
14 - (> 60.000 ≤ 80.000)
15 - (> 80.000 ≤ 100.000)
16 - (> 100.000' : 100)\n''')

area = fator_area[int(input('Qual o Tamanho da Área Edificada? '))]


# Captando a quantidade de cada infração cometida e fazendo append na lista acima que foram criadas vazias.
infra_leve2 = infra_leve.append(int(input('\nQuantas infrações leves foram cometidas? ')))

infra_media2 = infra_media.append(int(input('\nQuantas infrações médias foram cometidas? ')))

infra_grave2 = infra_grave.append(int(input('\nQuantas infrações graves foram cometidas? ')))

infra_gravissima2 = infra_gravissima.append(int(input('\nQuantas infrações gravíssimas foram cometidas? ')))

if infra_leve[0] <= 4 and infra_media[0] <= 4 and infra_grave[0] <= 4 and infra_gravissima[0] <= 2:
    multa = (2.5 * infra_leve[0] + 3.5 * infra_media[0] + 5 * infra_grave[0] + 7 * infra_gravissima[0]) * risco * area * vbbm
    print(f'\nA edificação fica Multada segundo a Lei 11.390/2020 no valor de R$ {multa}\n')
else:
    print('''
Você deve atentar para a quantidade máxima permitida à cada nível 
de infação a ser incluida no cálculo da Multa segundo a Lei 11.390.
''')