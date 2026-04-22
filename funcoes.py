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