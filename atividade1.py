# Implementação de Lista Dinâmica: 



# Complete o programa abaixo para que funcione a implementação de lista dinâmica.

# Foram adicionadas saídas esperadas que devem ser cumpridas como testes.




class DynamicIntArray:

    def __init__(self, capacity=2):

        if capacity <= 0:

            raise ValueError("Capacidade inicial deve ser maior que 0.")

        self.capacity = capacity        # Tamanho real do array interno

        self.size = 0                   # Quantos elementos o usuário colocou

        self.data = [0] * self.capacity # Cria Array estático interno (só de inteiros)



    # is_empty



    # get (faça validação de index fora dos limites.)



    # set (faça validação de index fora dos limites.)



    def append(self, value):

        if self.size == self.capacity:

            self._resize_up(2 * self.capacity)

        self.data[self.size] = value

        self.size += 1



    def _resize_up(self, new_capacity):

        print(f"⏫ Redimensionando de {self.capacity} para {new_capacity}")

        new_data = [0] * new_capacity

        for i in range(self.size):

            new_data[i] = self.data[i]

        self.data = new_data

        self.capacity = new_capacity



    # remove_at

    # remover elemento no index passado.

    # Reduzir a capacidade da Lista pela metade se 25% ou menos (<= 25%) do seu espaço estiver sendo usado

    # Exemplo, na lista de capacidade 8 com os seguintes valores [10, 99, 50],

    # ao remover um elemento sua capacidade deve cair de 8 para 4 e a lista ficar [10, 99] com capacidade 4. 

    # validar index fora dos limites.

    # retornar o valor removido.

    # Imprimir a seguinte mensagem quando for o caso: ⏬ Redimensionando de {self.capacity} para {new_capacity}



    # remove

    # remove o elemento buscado caso exista.

    # mesmas regras do remove_at.



    # insert_at
    def insert_at(self,value):
        for i in self.data:
            if i == value:
                return True
            
        lista.append(value)

    # com os parametros de index e valor a ser inserido.

    # respeitando as regras de aumento da lista.



    # index_of
    def index_of(self,value):
        cont = 0
        for i in self.data:
            if i == value:
                return cont 
            cont += 1
        return -1

    # retorna o index do valor buscado ou -1 caso não exista.



    # contains
    def contains(self,value):
        for i in self.data:
            if i == value:
                return True 
        return False


    # retorna True ou False se encontrou ou não o valor buscado.



    def __str__(self):

        return str(self.data[:self.size])

   




lista = DynamicIntArray()



lista.append(10)
lista.append(20)
lista.append(30)

print(lista)
print("Index do 10 é: ", lista.index_of(30))

print("10 existe na lista? ", "Sim" if lista.contains(10) else "Não")

print("adicionando o 40 na lista ", "ja existe na lista" if lista.insert_at(40) else "inseriu")

print(lista)


"""
print("Adicionando o 10;")

lista.append(10)

#Saída: Lista:  [10] 

print("Lista: ", lista)



print("Verificando se 0 existe;")

#Saída: "0 existe na lista? Não" 

print("0 existe na lista? ", "Sim" if lista.contains(0) else "Não")



print("Adicionando o 20;")

lista.append(20)

#Saída: Lista:  [10, 20] 

print("Lista: ", lista)



print("Verificando o index do 20;")

#Saída: "Index do 20 é: 1" 

print("Index do 20 é: ", lista.index_of(20))



print("Verificando se 20 existe;")

#Saída: "20 existe na lista? Sim" 

print("20 existe na lista? ", "Sim" if lista.contains(20) else "Não")



print("Adicionando o 30;")

lista.append(30)

print("Lista: ", lista)

print("Tamanho da Lista para o usuário: ", lista.size)

print("Tamanho real da Lista internamente: ", lista.capacity)

print()




print("Adicionando o 40;")

lista.append(40)

print("Lista: ", lista)



print("Adicionando o 50;")

lista.append(50)

# Saída: [10, 20, 30, 40, 50]   

print("Lista: ", lista)        



# Buscar Elemento no índice 2 

# Saída: 30  

print("Elemento na posição 2: ", lista.get(2))    



# Trocar Elemento no índice 2 para 99

# Saída: [10, 20, 99, 40, 50]

print("Trocando elemento no índice 2 para 99.")  

lista.set(2, 99)

print("Lista: ", lista)      



# Remover Elemento 40 se existir 

# Saída: [10, 20, 99, 50]

print("Removendo elemento 40 se existir.")

lista.remove(40)

print("Lista: ", lista)



print("Removendo elemento no indice 1 se existir.")

# Saída: [10, 99, 50]

lista.remove_at(1)

print("Lista: ", lista)



print("Removendo mais um elementos no indice 2.")

# Saída: Redimensionando de 8 para 4

# Saída: [10, 99]

lista.remove_at(2)

print("Lista: ", lista)



print("Removendo mais um elementos no indice 0.")

# Saída: Redimensionando de 4 para 2

# Saída: [10]

lista.remove_at(0)

print("Lista: ", lista)
"""