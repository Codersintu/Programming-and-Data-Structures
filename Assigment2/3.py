class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def minValue(node):
    current = node
    while current.left:
        current = current.left
    return current



def inorderSuccessor(root, k):
    # Case 1: Node has right subtree
    if k.right:
        return minValue(k.right)
    
    successor = None
    current = root
    while current:
        if k.data < current.data:
            successor = current
            current = current.left
        elif k.data > current.data:
            current = current.right
        else:
            break
    return successor



root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

k = root.left  

successor = inorderSuccessor(root, k)

if successor:
    print("Inorder Successor of", k.data, "is", successor.data)
else:
    print("Inorder Successor of", k.data, "is -1")
