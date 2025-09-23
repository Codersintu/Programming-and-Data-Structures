
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, data):
        # adding element
        new_node = Node(data)
        if self.rear is None: 
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        # removing element
        if self.front is None:
            return "Queue is empty"
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:  
            self.rear = None
        self._size -= 1
        return removed_data

    def peek(self):
        if self.front is None:
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        return self.front is None

    def size(self):
        return self._size


myQueue = Queue()
myQueue.enqueue("azoo")
myQueue.enqueue("halchal")
print("Front:", myQueue.peek())      
print("Dequeued:", myQueue.dequeue())
print("Front after dequeue:", myQueue.peek())
print("Size:", myQueue.size())
