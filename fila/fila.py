from stack import Stack

class Queue:
    def __init__(self):

        self.stack_enfileira = Stack()
        self.stack_desenfileira = Stack()

    def enqueue(self, data):

        self.stack_enfileira.push(data)

    def dequeue(self):

        if self.stack_desenfileira.is_empty():
            while not self.stack_enfileira.is_empty():
                self.stack_desenfileira.push(self.stack_enfileira.pop())
        
        if self.stack_desenfileira.is_empty():
            raise IndexError("Fila vazia - impossível desenfileirar.")

        return self.stack_desenfileira.pop()

    def is_empty(self):
        
        return self.stack_enfileira.is_empty() and self.stack_desenfileira.is_empty()


fila = Queue()

fila.enqueue("A")
fila.enqueue("B")
fila.enqueue("C") 
print(fila.dequeue())  
print(fila.dequeue())  
fila.enqueue("D")
print(fila.dequeue())  
print(fila.dequeue())  
