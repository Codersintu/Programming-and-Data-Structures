# 25/09/2025
# AVL Tree Implementation in Python
# A type of binarysearch tree
# AVL tree is a self-balancing binary search tree
# Balance-factor=a nodes balance factor is the different in subtree height
# Balance factor = height(left subtree) - height(right subtree)
# balance factor values=
# 0-the node is perfectly balanced
# >0-the node is right heavy
# <0-the node is left heavy
# if BF(x)>1-x is right heavy and unbalanced
# if BF(x)<-1-x is left heavy and unbalanced

# different case of unbalanced node
# case-1:left-left case-

# Node class delete method
class Node:
    def __init__(self):
        pass