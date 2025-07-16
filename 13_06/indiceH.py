def indice_h_linear(citacoes):
    for i in range(len(citacoes)):
        h = i + 1
        if citacoes[i] < h:
            return i
    return len(citacoes)



def indice_h_binaria(citacoes):
    inicio = 0
    fim = len(citacoes) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if citacoes[meio] >= meio + 1:
            inicio = meio + 1
        else:
            fim = meio - 1
    return inicio


citacoes = [10, 8, 5, 4,2]


print("Índice-h (Busca Linear):", indice_h_linear(citacoes))
print("Índice-h (Busca Binária):", indice_h_binaria(citacoes))