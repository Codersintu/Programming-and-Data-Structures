class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printSpiral(root):
    if not root:
        return
    

    s1 = []  
    s2 = [] 

    s1.append(root)

    while s1 or s2:


        while s1:
            temp = s1.pop()
            print(temp.data, end=" ")

            
            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)

        while s2:
            temp = s2.pop()
            print(temp.data, end=" ")

            
            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)



root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)

print("Spiral Order Traversal:")
printSpiral(root)
