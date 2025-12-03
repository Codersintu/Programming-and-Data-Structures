class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def count_leaves(self, root):
        if root is None: return 0
        if root.left is None and root.right is None:return 1
        
        return self.count_leaves(root.left) + self.count_leaves(root.right)
    
    def count_non_leaves(self, root):
        if root is None:return 0
        if root.left is None and root.right is None:return 0
        return self.count_non_leaves(root.left) + self.count_non_leaves(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.right=Node(6)

print("Leaf count:", root.count_leaves(root))         # expected 3 (nodes 4,5,6)
print("Non-leaf count:", root.count_non_leaves(root)) # expected 3 (nodes 1,2,3)