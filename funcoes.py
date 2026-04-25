from random import randint

def rolar_dados(quantidade):
    lista_dados = []

    for i in range(quantidade):
        lista_dados.append(randint(1, 6))
    
    return lista_dados

def guardar_dado(dados_rolados, dados_guardados, indice):
    lista_retorno = []

    lista_retorno.append(dados_rolados)
    lista_retorno.append(dados_guardados)

    lista_retorno[1].append(lista_retorno[0][indice])
    lista_retorno[0].pop(indice)

    return lista_retorno

def remover_dado(dados_rolados, dados_guardados, indice):
    lista_retorno = []

    lista_retorno.append(dados_rolados)
    lista_retorno.append(dados_guardados)

    lista_retorno[0].append(lista_retorno[1][indice])
    lista_retorno[1].pop(indice)

    return lista_retorno

def calcula_pontos_regra_simples(dados_rolados):
    dic_retorno = {1: 0, 
                   2: 0, 
                   3: 0, 
                   4: 0, 
                   5: 0, 
                   6: 0}

    for num in dados_rolados:
        dic_retorno[num] = dados_rolados.count(num) * num
    
    return dic_retorno

def calcula_pontos_soma(dados_rolados):
    soma = 0

    for num in dados_rolados:
        soma += num

    return soma

def calcula_pontos_sequencia_baixa(dados_rolados):
    seq_baixa = 0

    for dado in dados_rolados:
        if dado + 1 in dados_rolados and dado + 2 in dados_rolados and dado + 3 in dados_rolados:
            seq_baixa = 15
            break
    
    return seq_baixa

def calcula_pontos_sequencia_alta(dados_rolados):
    seq_alta = 0

    for dado in dados_rolados:
        if dado + 1 in dados_rolados and dado + 2 in dados_rolados and dado + 3 in dados_rolados and dado + 4 in dados_rolados:
            seq_alta = 30
            break
    
    return seq_alta

def calcula_pontos_full_house(dados_rolados):
    full_house = 0
    qtd_restricao = 0

    for dado in dados_rolados:
        if dados_rolados.count(dado) == 3 or dados_rolados.count(dado) == 2:
            full_house += dado
            qtd_restricao += 1
    
    if qtd_restricao != 5:
        return 0    
    else:
        return full_house

def calcula_pontos_quadra(dados_rolados):
    soma = 0

    for dado in dados_rolados:
        if dados_rolados.count(dado) >= 4:
            for dado in dados_rolados:
                soma += dado
            break

    return soma

def calcula_pontos_quina(dados_rolados):
    for dado in dados_rolados:
        if dados_rolados.count(dado) >= 5:
            return 50
    return 0
