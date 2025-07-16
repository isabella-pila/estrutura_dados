def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2][0]
        left = [x for x in arr if x[0] < pivot]
        middle = [x for x in arr if x[0] == pivot]
        right = [x for x in arr if x[0] > pivot]
        return quick_sort(left) + middle + quick_sort(right)
def two_sum_sorted(nums, target):

    nums_com_indices = [(num, i) for i, num in enumerate(nums)]
    nums_ordenados = quick_sort(nums_com_indices)
    esquerda, direita = 0, len(nums_ordenados) - 1
    while esquerda < direita:
        soma_atual = nums_ordenados[esquerda][0] + nums_ordenados[direita][0]

        if soma_atual == target:
            return [nums_ordenados[esquerda][1], nums_ordenados[direita][1]]
        elif soma_atual < target:
            esquerda += 1
        else:
            direita -= 1
def two_sum_hash(numeros, alvo):
    
        indice_por_valor = {}  
        
        for i, valor_atual in enumerate(numeros):
            complemento = alvo - valor_atual
            
            if complemento in indice_por_valor:
                
                return [indice_por_valor[complemento], i]
        
            indice_por_valor[valor_atual] = i
            

def two_sum(numeros, alvo):
    indice_por_valor = {}  

    for i, valor_atual in enumerate(numeros):
        complemento = alvo - valor_atual
        if complemento in indice_por_valor:
            return [indice_por_valor[complemento], i]
        indice_por_valor[valor_atual] = i

       



if __name__ == "__main__":

    numeros = [2, 7, 11, 15]

    alvo = 9

    resultado = two_sum(numeros, alvo)

    print(resultado)  # saída esperada: [0, 1]

    numeros = [2, 7, 11, 15]
    alvo = 9
    resultado = two_sum_brute_force(numeros, alvo)
    print(f"Solução com Força Bruta: {resultado}")  # Saída esperada: [0, 1]

    numeros = [3, 2, 4]
    alvo = 6
    resultado = two_sum_brute_force(numeros, alvo)
    print(f"Solução com Força Bruta: {resultado}")  # Saída esperada: [1, 2]

    numeros = [2, 7, 11, 15]
    alvo = 9
    resultado = two_sum_sorted(numeros, alvo)
    print(f"Solução com Vetor Ordenado: {resultado}")  # Saída esperada: [0, 1]

    numeros = [3, 2, 4]
    alvo = 6
    resultado = two_sum_sorted(numeros, alvo)
    # A saída pode ser [2, 1] ou [1, 2] dependendo da estabilidade da ordenação
    print(f"Solução com Vetor Ordenado: {sorted(resultado)}") 


    numeros = [2, 7, 11, 15]
    alvo = 9
    resultado = two_sum_hash(numeros, alvo)
    print(f"Solução com Hash Map: {resultado}")  # Saída esperada: [0, 1]

    numeros = [3, 2, 4]
    alvo = 6
    resultado = two_sum_hash(numeros, alvo)
    print(f"Solução com Hash Map: {resultado}")  # Saída esperada: [1, 2]