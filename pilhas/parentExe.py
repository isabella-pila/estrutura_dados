# Dado uma string de expressão x. 
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e 
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):

    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """

    pilha = Stack()

    for caractere in expression:
        if caractere == '(':
            pilha.push('(')  # Sempre que encontrar um '(', empilha
        elif caractere == ')':
            if pilha.is_empty():
                return False  # Se tentar fechar um parêntese e a pilha estiver vazia, está errado
            pilha.pop()  # Remove um '(' da pilha, pois achamos o parêntese que fecha

    return pilha.is_empty()  # Se a pilha estiver vazia no final, está tudo certo



# Teste
#print(is_balanced("[{}(2+2)]{}")) #Esperado True
#print(is_balanced("[{}(2+2))]{}")) #Esperado False
#print(is_balanced("[{}])")) #Esperado False