# date 09/9/2025
# insertion of a node in Existing linked list
# case-1 insert at the beginning
# class Node:
#   def __init__(self,data):
#     self.data=data
#     self.next=None


# nodeNew=Node("s")

# def insertNodeAtPosition(head,nodeNew,position):
# #   case-1:inserting at the begining
#     if position==1:
#        nodeNew.next=head
#        return nodeNew
    


















# Doubly linked list
# node- have three blocks/information
class Node:
   def __init__(self,data):
      self.data=data
      self.prev=None
      self.next=None



node1=Node("s")
node2=Node("I")
node3=Node("N")
node4=Node("T")
node5=Node("U")

node1.next=node2

node2.prev=node1
node2.next=node3

node3.prev=node2
node3.next=node4

node4.prev=node3
node4.next=node5
node5.prev=node4

# definition for traversal
def traversal(head):
  currentNode=head
  while currentNode:
    print(currentNode.data,end="->")
    currentNode=currentNode.next
  print("null")


def reverse_traversal(tail):
    currentNode = tail
    while currentNode:
        print(currentNode.data, end="->")
        currentNode = currentNode.prev
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

# definiton to reverse delete a node
def delete_reverse_Node(tail,nodeToDelete):
#   case:1 if node to be deleted is head node itself
    if tail==nodeToDelete:
     if tail==None:
      return tail.prev
    # case:2 if node to be deleted is in b/w node
    
    currentNode=tail
    while currentNode.prev and currentNode.prev != nodeToDelete:
      currentNode=currentNode.prev

    currentNode.prev=currentNode.prev.prev

    return tail

# Example: start from node5 (tail)
# reverse_traversal(node5)
traversal(node1)
node1=deleteNode(node1,node3)
node5=delete_reverse_Node(node5,node1)
traversal(node1)





