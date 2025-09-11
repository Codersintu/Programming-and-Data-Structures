# circular list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def traversal(head):
    if head is None:
        print("List is empty")
        return
    
    current = head
    while True:
        print(current.data, end="->")
        current = current.next
        if current == head:   # stop when cycle completes
            break
    print("HEAD")
def insert_at_beginning(head, data):
    new_node = Node(data)
    
    if head is None:
        new_node.next = new_node   # single node points to itself
        return new_node
    
    # find last node
    last = head
    while last.next != head:
        last = last.next
    
    new_node.next = head
    last.next = new_node
    head = new_node
    
    return head
def insert_at_beginning(head, data):
    new_node = Node(data)
    
    if head is None:
        new_node.next = new_node   # single node points to itself
        return new_node
    
    # find last node
    last = head
    while last.next != head:
        last = last.next
    
    new_node.next = head
    last.next = new_node
    head = new_node
    
    return head


def delete_head(head):
    if head is None:
        return None
    
    # case: only one node
    if head.next == head:
        return None
    
    # find last node
    last = head
    while last.next != head:
        last = last.next
    
    last.next = head.next 
    head = head.next     
    return head
