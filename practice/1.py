# linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def traversal(head):
        currentNode=head
        while currentNode:
            print(currentNode.data,end="->")
            currentNode=currentNode.next
        print("null")

def nodeTodelete(head,nodeToDelete):
     if head==nodeToDelete:
        return head.next
     
     currentNode=head
     while currentNode.next and currentNode.next != nodeToDelete:
          currentNode=currentNode.next
     
     currentNode.next=currentNode.next.next
     return head

def insertAtPosition(Head,newNode,position):
     if position==1:
          newNode.next=Head
          return newNode
     currentNode=Head
     for _ in range(position-2):
         if currentNode is None:
              raise Exception("position out of bounds")
     currentNode=currentNode.next
     newNode.next=currentNode.next
     currentNode.next=newNode
     return Head

           
node1=Node("sintu")
node2=Node("rahul")
node3=Node("chotu")
node4=Node("vikash")

node1.next=node2
node2.next=node3
node3.next=node4

traversal(node1)
delete=nodeTodelete(node1,node3)
traversal(node1)
head = insertAtPosition(node1, node3, 3)
traversal(head)