class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def getHeight(root):
    if not root:
        return 0
    return root.height


def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)


def rightRotate(y):
    print("Right Rotation (LL case)")
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))

    return x


def leftRotate(x):
    print("Left Rotation (RR case)")
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y


def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)

    # Rotations
    if balance > 1 and key < root.left.key:
        return rightRotate(root)

    if balance < -1 and key > root.right.key:
        return leftRotate(root)

    if balance > 1 and key > root.left.key:
        print("Left-Right Rotation (LR case)")
        root.left = leftRotate(root.left)
        return rightRotate(root)

    if balance < -1 and key < root.right.key:
        print("Right-Left Rotation (RL case)")
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root


def getMinValueNode(root):
    current = root
    while current.left:
        current = current.left
    return current


def deleteNode(root, key):
    if not root:
        return root


    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
    
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp


        temp = getMinValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)


    if root is None:
        return root
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    
    balance = getBalance(root)


    # Left Left
    if balance > 1 and getBalance(root.left) >= 0:
        print("Right Rotation (LL case) after deletion")
        return rightRotate(root)

    # Left Right
    if balance > 1 and getBalance(root.left) < 0:
        print("Left-Right Rotation (LR case) after deletion")
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # Right Right
    if balance < -1 and getBalance(root.right) <= 0:
        print("Left Rotation (RR case) after deletion")
        return leftRotate(root)

    # Right Left
    if balance < -1 and getBalance(root.right) > 0:
        print("Right-Left Rotation (RL case) after deletion")
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root


def preOrder(root):
    if not root:
        return
    print(root.key, end=" ")
    preOrder(root.left)
    preOrder(root.right)


root = None
keys = [20, 4, 26, 3, 9, 15]

for key in keys:
    root = insert(root, key)

print("Preorder before deletion:")
preOrder(root)

root = deleteNode(root, 26)
print("\nPreorder after deletion of 26:")
preOrder(root)
