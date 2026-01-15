"""
DESAFIO: Gestão de Combustível - Motoristas
Data: 14 de janeiro de 2026
"Oi, Jonathan! Tudo bem? Cara, estou com um problema chato. Eu tenho 5 motoristas e eles estão gastando muito com combustível,
mas eu não consigo saber quem está sendo eficiente e quem está 'pisando fundo' demais.
Eu tenho as anotações de cada viagem em um papel: o nome do motorista, quantos quilômetros ele
rodou e quantos litros de combustível ele usou para aquela quilometragem.
Eu precisava de um programa onde eu pudesse jogar esses dados e ele me desse um relatório real. Quero saber quem
tem a melhor média (km por litro) e,
principalmente, quem está com a média abaixo de 10 km/l, porque esses eu vou ter que chamar para conversar.
Ah, e se puder me dar o custo total que eu tive, sabendo que a gasolina está R$ 5,80, seria perfeito para o meu financeiro!"
"""

print('Gastos por Viagem')
# Confirmação, se o usuário colocara o caracter correto
while True:
    try:
        quantidade_funcionarios = int(float(input('Quantos funcionários quer calcular?: ')))
        break
    except ValueError:
        print("Erro: Digite um número inteiro válido.")
nomes = [] # Aqui guardamos a listas de nomes digitados nos inputs
relatorios_funcionarios = [] # Aqui vamos guardar os dados brutos (gasolina, km, viagens)
media_final = [] # Aqui vamos guardar as médias (m1, m2, m3) de cada um
valor_gasolina = []

while True:
    try:
        gasolina = float(input(('digite o valor da gasolina hoje: ')))
        valor_gasolina.append(gasolina)
        break
    except ValueError:
        print('Erro: Digite um número inteiro válido! '
              'Lembresse de usar . ao invés de ,')

# Aqui colocamos os nomes na lista
for quantidade in range(quantidade_funcionarios):
    funcionarios = input(f'Digite os nomes dos funcionários {quantidade+1}º: ')
    nomes.append(funcionarios)

# Aqui pegamos os nomes das listas e verificamos
for i, nome in  enumerate(nomes, 1):
    gasolina = float(input(f'O funcionário \n{i} - {nome} \nUsou quanto de gasolina?: '))
    km_rodados = int(input(f'O funcionário \n{i} - {nome} \nRodou quantos Km?: '))
    viagens = int(input(f'O funcionário \n{i} - {nome} \nFez quantas Viagens?: '))

    # Calculo necessário para resolver as médias
    media1 = gasolina / km_rodados if km_rodados > 0 else 0
    media2 = km_rodados / viagens if viagens > 0 else 0
    media3 = gasolina / viagens if viagens > 0 else 0

    media_final += media1, media2, media3

    relatorio = gasolina, km_rodados, viagens
    relatorios_funcionarios.append(relatorio) # Devolvendo para Lista

    # Mantendo suas variáveis de atribuição originais
    gasolina, km_rodados, viagens = relatorio[0], relatorio[1], relatorio[2]
    relatorio1 = media1
    relatorio2 = media2
    relatorio3 = media3

# --- LÓGICA PARA IDENTIFICAR O MELHOR (MAIOR KM/L) ---
todas_m1 = media_final[::3]
melhor_media = min(todas_m1)
quem_e_o_melhor = nomes[todas_m1.index(melhor_media)]

# Comentários
print('\n' + '='*40)
print('       RELATÓRIO GERAL ACUMULADO')
print('='*40)

total_gasto_empresa = 0

for indice, nome in enumerate(nomes):
    # Cálculo automático para buscar o trio de médias de cada funcionário
    posicao_base = indice * 3 # Pulando de 3 em 3 no indice da lista nomes

    m1 = media_final[posicao_base]
    m2 = media_final[posicao_base + 1]
    m3 = media_final[posicao_base + 2]

    # Acesso ao total de gasolina do relatório para o financeiro
    gasolina_total = relatorios_funcionarios[indice][0]
    custo_motorista = gasolina_total * valor_gasolina[0]
    total_gasto_empresa += custo_motorista
    print(f'\nFuncionário: {nome}')
    print(f'Com a gasolina a {valor_gasolina[0]}')
    print(f'-> Média Km/L: {m1:.2f}Lts')

    # Lógica solicitada pelo cliente: média abaixo de 10 km/l gera alerta
    if m3 > 10:
        print(f'   ⚠️ ALERTA: Rendimento baixo ({m1:.2f} L/Km)! Chamar para conversar.')

    print(f'-> Média Km/Viagem: {m2:.2f}Lts')
    print(f'-> Média Lts/Viagem: {m3:.2f}Lts')
    print(f'-> Custo Total deste Motorista: R$ {custo_motorista:.2f}')
    print('-' * 30)

print('\n' + '='*40)
print(f'MOTORISTA MAIS EFICIENTE: {quem_e_o_melhor} ({melhor_media:.2f} L/Km)')
print(f'INVESTIMENTO TOTAL EM COMBUSTÍVEL: R$ {total_gasto_empresa:.2f}')
print('='*40)