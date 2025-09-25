# 18/09/25
# Binary search tree(BST):A binary tree where the following property
# must be true for any node "X" in the tree
# 1)the x node's left child and all of its descedants(children, children's children and so on)
# have lower values than x's value

# (2)the right child and all its descendants have higher values than
# "x" value
# 
# (3) left and right subtree must also be BST

# all nodes in left substance of x is less than of mainroot

# all node in the right substanceof x is greater than mainroot

# Searching in BST:
class Node:
 def __init__(self,data):
        self.data = data
        self.right=None
        self.left=None

def inorder(root):
        if root is not None:
            inorder(root.left)
            print(root.value,end=" ")
            inorder(root.right)

def traversal(root):
    if root is not None:
        traversal(root.left)
        print(root.data,end=" ")
        traversal(root.right)

def insert(root,key):
    if root is None:
     return Node(key)
    else:
        if root.data==key:
            return root
        elif key<root.data:
            root.left=insert(root.left,key)
        else:
            root.right=insert(root.right,key)
    return root


root=Node(10)
root.left=Node(5)
root.right=Node(7)
root.left.left=Node(4)
root.left.right=Node(3)
root.right.left=Node(15)
root.right.right=Node(11)

def search(node,target):
    if node is None:
        return None
    elif node.data==target:
        return node
    elif target<node.data:
        return search(node.left,target)
    else:
        return search(node.right,target)
    

print(search(root,4))

# inserting a node in BST
# start at the root node
# compare each node :
# (a) is the value lower go left side
# (b)if the value higher go right side
# continue to compare nodes with now value untill there is no right & left to 


# last class in week thursday 18 hai for more go iit10.py file******************************
