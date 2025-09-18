# A new Datastructure 
# Leaf Node-which node has no child is called leaf node
# child is reflecting of branches 
# Binary Trees:A type of tree datastructure where each node have a maximum of two child nodes
# maximum means may have 0,1,2 child

# creation of binary tree
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

# creation of tree nodes as an object of treenode class
root=TreeNode("R")
nodeA=TreeNode("A")
nodeB=TreeNode("B")
nodeC=TreeNode("C")
nodeD=TreeNode("D")
nodeE=TreeNode("E")
nodeF=TreeNode("F")
nodeG=TreeNode("G")
nodeH=TreeNode("H")
nodeI=TreeNode("I")

root.left=nodeA
root.right=nodeB

nodeA.left=nodeC
nodeA.right=nodeD

nodeB.left=nodeE
nodeB.right=nodeF

nodeC.left=nodeG

# Test
print(root.right.right.data)


# end class go iit7.py file

