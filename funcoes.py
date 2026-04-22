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

dados_rolados = [2, 2, 2, 2]
dados_no_estoque = [1]
dado_para_remover = 0

print(remover_dado(dados_rolados, dados_no_estoque, dado_para_remover))

