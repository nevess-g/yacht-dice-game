from random import randint

def rolar_dados(quantidade):
    lista_dados = []

    for i in range(quantidade):
        lista_dados.append(randint(1, 6))
    
    return lista_dados
