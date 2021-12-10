from reportlab.pdfgen import canvas
import uuid

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


# Apresentar a Seleção de Infrações Leves encontradas
print('''
INFRAÇÕES LEVES:
0. Não Houveram Infrações Leves.
1. Acesso de viatura deficiente quanto à localização ou às dimensões.
2. Isolamento de risco deficiente.
3. Resistência ao fogo dos elementos de construção deficiente.
4. Compartimentação deficiente.
5. Controle de material de acabamento e de revestimento deficiente.
6. Saída de emergência deficiente.
7. Elevador de emergência deficiente.
8. Sistema de pressurização da escada deficiente.
9. Sistema de controle de fumaça deficiente.
10. Plano de emergência deficiente.
11. Brigada de incêndio ou bombeiro civil deficiente.
12. Bombeiro civil não credenciado junto ao Corpo de Bombeiros Militar.
13. Sistema de iluminação de emergência deficiente.
14. Sistema de detecção de incêndio deficiente.
15. Sistema de alarme de incêndio deficiente.
16. Sinalização de emergência deficiente.
17. Sistema de extintores de incêndio deficiente.
18. Sistema de hidrantes ou mangotinhos deficiente.
19. Sistema de chuveiros automáticos deficiente.
20. Sistema de resfriamento deficiente.
21. Sistema de proteção por espuma deficiente.
22. Sistema fixo de gases para combate a incêndio deficiente.
23. Instalações elétricas prediais em desconformidade com a legislação.
24. Documentação em desconformidade com a legislação.
25. Certificação do Corpo de Bombeiros Militar não afixada em local visível ao público.\n''')

# Captando a quantidade de infrações Leves cometidas e fazendo append na lista acima que foram criadas vazias.
infra_leve2 = infra_leve.append(int(input('Quantas infrações leves foram cometidas? ')))


# Apresentar a Seleção de Infrações MÉDIAS encontradas
print('''
INFRAÇÕES MÉDIAS:
0. Não Houveram Infrações Médias.
1. Elemento automatizado de compartimentação inoperante.
2. Saída de emergência inoperante.
3. Elevador de emergência inoperante.
4. Sistema de pressurização da escada inoperante.
5. Sistema de controle de fumaça inoperante.
6. Brigada de incêndio ou bombeiro civil reprovado na avaliação de desempenho.
7. Sistema de iluminação de emergência inoperante.
8. Sistema de detecção de incêndio inoperante.
9. Sistema de alarme de incêndio inoperante.
10. Sistema de extintores de incêndio inoperante.
11. Sistema de hidrantes ou mangotinhos inoperante.
12. Sistema de chuveiros automáticos inoperante.
13. Sistema de resfriamento inoperante.
14. Sistema de proteção por espuma inoperante.
15. Sistema fixo de gases para combate a incêndio inoperante.
16. Armazenamento de líquidos inflamáveis em desconformidade com a legislação.
17. Armazenamento e utilização de gás liquefeito de petróleo (GLP) em desconformidade com a legislação.
18. Armazenamento e utilização de gás natural (GN) em desconformidade com a legislação.
19. Materiais ou equipamentos de sistemas de segurança contra incêndios e emergências sem certificação, quando exigida.
20. Deixar de atualizar o Projeto Técnico em decorrência de mudança de altura, de área ou de categoria de divisão da ocupação \
da edificação ou área de risco, quando tais alterações não implicam em redimensionamento das medidas de segurança contra incêndios \
e emergências constantes nas Tabelas do Anexo “A” da norma técnica de procedimentos administrativos.
''')

# Captando a quantidade de infrações Leves cometidas e fazendo append na lista acima que foram criadas vazias.
infra_media2 = infra_media.append(int(input('Quantas infrações médias foram cometidas? ')))

# Apresentar a Seleção de Infrações GRAVES encontradas
print('''
INFRAÇÕES GRAVES:
0. Não Houveram Infrações Graves.
1. Acesso de viatura inexistente.
2. Isolamento de risco inexistente.
3. Resistência ao fogo dos elementos de construção inexistente.
4. Compartimentação inexistente.
5. Controle de material de acabamento e de revestimento inexistente.
6. Saída de emergência inexistente.
7. Elevador de emergência inexistente.
8. Sistema de pressurização da escada inexistente.
9. Sistema de controle de fumaça inexistente.
10. Plano de emergência inexistente.
11. Brigada de incêndio ou bombeiro civil inexistente.
12. Sistema de iluminação de emergência inexistente.
13. Sistema de detecção de incêndio inexistente.
14. Sistema de alarme de incêndio inexistente.
15. Sinalização de emergência inexistente.
16. Sistema de extintores de incêndio inexistente.
17. Sistema de hidrantes ou mangotinhos inexistente.
18. Sistema de chuveiros automáticos inexistente.
19. Sistema de resfriamento inexistente.
20. Sistema de proteção por espuma inexistente.
21. Sistema fixo de gases para combate a incêndio inexistente.
22. Sistema elétrico de alimentação dos equipamentos de segurança contra incêndios e emergências \
desprotegido contra a ação do fogo.
23. Sistema de proteção contra descargas atmosféricas inexistente.
24. Armazenamento e utilização de produtos perigosos em desconformidade com a legislação.
25. Falta de cumprimento das medidas de segurança contra incêndios e emergências após encerramento \
da vigência do Termo de Autorização para Adequação do Corpo de Bombeiros Militares - TAACBM.
26. Deixar de atualizar o Projeto Técnico em decorrência de mudança de leiaute, de altura, de área \
ou de categoria de divisão da ocupação da edificação ou área de risco, quando tais alterações implicam \
em novas exigências ou redimensionamento das medidas de segurança contra incêndios e emergências constantes \
nas Tabelas do Anexo “A” da norma técnica de procedimentos administrativos.
27. Uso indevido de logomarca, brasão, insígnias, uniformes e demais sinais ou símbolos idênticos ou semelhantes \
aos de uso privativo dos Corpos de Bombeiros Militares.
''')

# Captando a quantidade de infrações Graves cometidas e fazendo append na lista acima que foram criadas vazias.
infra_grave2 = infra_grave.append(int(input('Quantas infrações graves foram cometidas? ')))


# Apresentar a Seleção de Infrações GRAVÍSSIMAS encontradas
print('''
INFRAÇÕES GRAVÍSSIMAS:
0. Não Houveram Infrações Gravíssimas.
1. Realização de evento temporário sem a devida Licença do Corpo de Bombeiros
Militar.
2. Armazenamento, comércio ou manipulação de explosivos em desconformidade
com a legislação.
3. Edificação ou área de risco sem Certificação do Corpo de Bombeiros Militar.
4. Local destinado à reunião de público com lotação acima do permitido.
5. Local destinado à reunião de público com saída de emergência insuficiente, obstruída ou trancada.
''')

infra_gravissima2 = infra_gravissima.append(int(input('Quantas infrações gravíssimas foram cometidas? ')))

if infra_leve[0] <= 4 and infra_media[0] <= 4 and infra_grave[0] <= 4 and infra_gravissima[0] <= 2:
    multa = round((2.5 * infra_leve[0] + 3.5 * infra_media[0] + 5 * infra_grave[0] + 7 * infra_gravissima[0]) * risco * area * vbbm, 2)
    multa_formatada = str(multa).replace('.', ',')
    print(f'\nA edificação fica Multada segundo a Lei 11.390/2020 no valor de R$ {multa}\n')
else:
    print('''
Você deve atentar para a quantidade máxima permitida à cada nível 
de infação a ser incluida no cálculo da Multa segundo a Lei 11.390.
''')
    

def GeneratePDF(multa):
    try:
        nome_pdf = 'Multa por Infração'
        pdf = canvas.Canvas(f'{nome_pdf}.pdf')
        pdf.setTitle(nome_pdf)
        # CABEÇALHO
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(222,800, 'ESTADO DO MARANHÃO')
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(173,784, 'SECRETARIA DE SEGURANÇA PÚBLICA')
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(144,768, 'CORPO DE BOMBEIROS MILITAR DO MARANHÃO')
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(180,752, 'DIRETORIA DE ATIVIDADES TÉCNICAS')
        
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(115,715, 'MULTA POR INFRAÇÃO Nº {} - DAT'.format(uuid.uuid1()))
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(70,666, 'A edificação por infringir a Lei 11.390, fica Multada:')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(55,624, 'Valor da Multa')
        pdf.drawString(57,604, f'R$ {multa}')
        pdf.save()
        print(f'{nome_pdf}.pdf criado com sucesso!')
    except:
        print(f'Erro ao gerar {nome_pdf}.pdf')
        
multa = multa_formatada

GeneratePDF(multa)