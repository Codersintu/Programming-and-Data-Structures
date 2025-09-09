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

# definition for traversal
def traversal(node4):
  currentNode=node4
  print(currentNode.data,end="->")
  while currentNode:
    print(currentNode.data,end="->")
    currentNode=currentNode.next
  print("null")

  traversal(node4)
