from funcoes import *

cartela = {
    'regra_simples':  {
        1:-1,
        2:-1,
        3:-1,
        4:-1,
        5:-1,
        6:-1
    },
    'regra_avancada' : {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

jogadas = 0

dados = [rolar_dados(5), []]

opcoes = ["1", "2", "3", "4", "0"]

combinacoes_possiveis = ["1", "2", "3", "4", "5", "6", 'cinco_iguais', 'full_house', 'quadra', 'sem_combinacao', 'sequencia_alta', 'sequencia_baixa']
combinacoes_jogadas = []

reroll = 0

while jogadas < 12:

    print(f"Dados rolados: {dados[0]}")
    print(f"Dados guardados: {dados[1]}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    selecao = input()

    while selecao not in opcoes:
        print("Opção inválida. Tente novamente.")
        selecao = input()
    
    match selecao:
        case "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice_dado = input()
            dados[1] = guardar_dado(dados[0], dados[1], int(indice_dado))[1]
        case "3":
            if reroll >= 2:     
                print("Você já usou todas as rerrolagens.")
            else:
                dados[0] = rolar_dados(len(dados[0]))
                reroll += 1
        case "0":
            print("Digite a combinação desejada:")
            combinacao = input()

            dados = dados[0] + dados[1]

            while combinacao not in combinacoes_possiveis or combinacao in combinacoes_jogadas:
                if combinacao not in combinacoes_possiveis:
                    print("Combinação inválida. Tente novamente.")
                elif combinacao in combinacoes_jogadas:
                    print("Essa combinação já foi utilizada.")
                combinacao = input()

            combinacoes_jogadas.append(combinacao)
            
            cartela = faz_jogada(dados, combinacao, cartela)

            dados = [rolar_dados(5), []]
            reroll = 0
            jogadas += 1

        case "4":
            imprime_cartela(cartela)

        case "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = input()
            remover_dado(dados[0], dados[1], int(indice))

imprime_cartela(cartela)

soma_simples = 0
soma_avancada = 0

for v in cartela['regra_simples'].values():
    if v != -1:
        soma_simples += v

for v in cartela['regra_avancada'].values():
    if v != -1:
        soma_avancada += v

if soma_simples >= 63:
    soma_avancada += 35

pontuacao = soma_simples + soma_avancada
print(f"Pontuação total: {pontuacao}")
