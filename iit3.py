# Linked List
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None


# definition for traversal
def traversal(head):
  currentNode=head
  while currentNode:
    print(currentNode.data,end="->")
    currentNode=currentNode.next
  print("null")


# definiton to delete a node
def deleteNode(head,nodeToDelete):
#   case:1 if node to be deleted is head node itself
    if head==nodeToDelete:
      return head.next
    # case:2 if node to be deleted is in b/w node
    
    currentNode=head
    while currentNode.next and currentNode.next != nodeToDelete:
      currentNode=currentNode.next

    currentNode.next=currentNode.next.next

    return head
  

# creating of object of node class
node1=Node("sintu")
node2=Node("mandep")
node3=Node("yash")
node4=Node("tripti")
node5=Node("novesh")

# link b/w nodes

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

traversal(node1)          # prints list
node1 = deleteNode(node1, node3)  # delete 'yash'
traversal(node1)   

