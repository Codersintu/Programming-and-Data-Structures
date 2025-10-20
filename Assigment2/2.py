class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1



def get_height(root):
    if not root:
        return 0
    return root.height



def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)



def right_rotate(y):
    x = y.left
    T2 = x.right


    x.right = y
    y.left = T2


    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x



def left_rotate(x):
    y = x.right
    T2 = y.left


    y.left = x
    x.right = T2

    # Update heights
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


# Insert node in AVL Tree
def insert(root, key):
    
    if not root:
        return Node(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    
    balance = get_balance(root)

    # Balancing
    # Case 1 - Left Left
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Case 2 - Right Right
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Case 3 - Left Right
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Case 4 - Right Left
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root



def print_balance_factors(root):
    if root:
        print_balance_factors(root.left)
        print(f"Node {root.key}: Balance Factor = {get_balance(root)}")
        print_balance_factors(root.right)



sequence = [10, 20, 30, 25, 28, 27, 5]

root = None
for key in sequence:
    root = insert(root, key)

print("\n Balance Factor of each node after insertion:")
print_balance_factors(root)
