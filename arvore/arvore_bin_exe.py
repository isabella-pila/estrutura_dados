class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None):
        node = Node(data)
        self.root = node

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.simetric_traversal(node.left)
        print(node)
        if node.right:
            self.simetric_traversal(node.right)
   
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
    
    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0  
            
        left_height = self.height(node.left) if node.left else 0
        right_height = self.height(node.right) if node.right else 0
        return 1 + max(left_height, right_height)

        

def example_tree():
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n2
    return tree
    
    


    #      '+'
    #    /     \
    #  'a'      '*'
    #          /   \
    #        'b'    '-'
    #              /    \
    #            '/'    'e' 
    #           /   \
    #         'c'   'd'

    
    # a + b * c / d - e (Simetrico - InOrder)
    # a b c d / e - * + (Pós Ordem - PostOrder)




if __name__ == '__main__':
    tree = example_tree()
    print("Simetrico - InOrder")
    tree.simetric_traversal() 
    
    tree2 = example_tree()
    print("")
    print("Pós Ordem - PostOrder")
    tree2.postorder_traversal() 


    # Altura da árvore inteira
    altura_total = tree.height()
    print(f"\nAltura da árvore inteira: {altura_total}")

    # Altura de um nó específico (exemplo: nó '-')
    no_menos = tree.root.right.right #navegando na árvore.
    altura_menos = tree.height(no_menos)
    print(f"Altura a partir do nó '{no_menos.data}': {altura_menos}")