def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr) // 2]
    esquerda = [x for x in arr if x < pivo]
    meio = [x for x in arr if x == pivo]
    direita = [x for x in arr if x > pivo]
    return quicksort(esquerda) + meio + quicksort(direita)


def busca_linear_com_quicksort(arr, alvo):
    arr_ordenado = quicksort(arr)
    for i in range(len(arr_ordenado)):
        if arr_ordenado[i] >= alvo:
            if arr_ordenado[i] == alvo:
                return i
            else:
                return i  # Inserir antes do atual
    return len(arr_ordenado)  # Inserir no final




def busca_binaria_com_quicksort(arr, alvo):
    arr_ordenado = quicksort(arr)
    inicio = 0
    fim = len(arr_ordenado) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr_ordenado[meio] == alvo:
            return meio
        elif arr_ordenado[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return inicio  


arr = [10, 3, 5, 8, 2]
alvo = 6

print("Array ordenado:", quicksort(arr))
print("Busca Linear:", busca_linear_com_quicksort(arr, alvo))
print("Busca Binária:", busca_binaria_com_quicksort(arr, alvo))