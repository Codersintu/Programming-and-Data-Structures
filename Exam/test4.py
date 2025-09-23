class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def remove_duplicates(self):
        seen = set()
        temp = self.head
        while temp:
            if temp.data in seen:
                
                nxt = temp.next
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:  
                    self.head = temp.next
                temp = nxt
            else:
                seen.add(temp.data)
                temp = temp.next

    def display(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result


dll = DoublyLinkedList()
for val in [1, 2, 3, 2, 4]:
    dll.append(val)

print("Before:", dll.display())  
dll.remove_duplicates()
print("After:", dll.display())   

dll2 = DoublyLinkedList()
for val in [8, 4, 6, 8, 4, 10, 12]:
    dll2.append(val)

print("Before:", dll2.display())  
dll2.remove_duplicates()
print("After:", dll2.display())   