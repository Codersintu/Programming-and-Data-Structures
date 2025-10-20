class Node:
    def __init__(self, data):
        self.data = data
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



def inorderTraversal(root, arr):
    if root:
        inorderTraversal(root.left, arr)
        arr.append(root.data)
        inorderTraversal(root.right, arr)


def kthSmallest(root, k):
    arr = []
    inorderTraversal(root, arr)
    if k <= len(arr):
        return arr[k-1]
    return -1


def kthLargest(root, k):
    arr = []
    inorderTraversal(root, arr)
    n = len(arr)
    if k <= n:
        return arr[n-k]
    return -1

root = None
elements = [20, 8, 22, 4, 12, 10, 14]

for el in elements:
    root = insert(root, el)

k = 3
print(f"{k}rd Smallest element:", kthSmallest(root, k))
print(f"{k}rd Largest element:", kthLargest(root, k))
