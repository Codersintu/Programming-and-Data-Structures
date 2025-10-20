class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def count_nodes(root):
    if root is None:
        return (0,0)
    
    if root.left is None and root.right is None:
        return (1,0)
    

    left_leaves, left_non_leaves = count_nodes(root.left)
    right_leaves, right_non_leaves = count_nodes(root.right)
    
    total_leaves = left_leaves + right_leaves
    total_non_leaves = left_non_leaves + right_non_leaves + 1
    
    return (total_leaves, total_non_leaves)

root=Node(10)
root.left=Node(8)
root.right=Node(13)
root.left.left=Node(5)
root.left.right=Node(6)
root.right.right=Node(14)
leaves, non_leaves = count_nodes(root)
print("Number of Leaf Nodes:", leaves)
print("Number of Non-Leaf Nodes:", non_leaves)
