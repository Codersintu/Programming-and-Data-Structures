# STACK
# LIFO=last in first out
# push=add a new element on the stack
# pop=remove return the top element
# peak=return the top(last) element on the stack
# isEmpty= checks if the stack is empty

# code
# Day=[]
# Push (add elements)
# Day.append("sunday")
# Day.append("monday")
# Day.append("tuesday")
# Day.append("wednesday")
# Day.append("thursday")
# Day.append("friday")
# Day.append("saturday")
# print("day after pushing", Day)
# print("size of stack is:", len(Day))
# print("top element is:", Day[-1])
# top_element = Day.pop()
# print("popped element is:", top_element)

# creating stack using class:
# class Stack:
#     def __init__(self):
#         self.stack=[]

#     def is_empty(self):
#             return len(self.stack) == 0
#     def push(self, name):
#             self.stack.append(name)
            
#     def pop(self):
#             if self.is_empty():
#                 return "stack is empty"
#             return self.stack.pop()
#     def peek(self):
#             if self.is_empty():
#                 return "stack is empty"
#             return self.stack[-1]

# mystack=Stack()
# mystack.push("sintu")
# mystack.push("rishi")
# print("stack after pop", mystack.pop())
# print("top element is:", mystack.peek())



# def reverse_string_using_stack(input_string):
#     stack=[]
#     for char in input_string:
#         stack.append(char)

#     reverse_string=""
#     while stack:
#         reversed_string += stack.pop()

#     return reverse_string
  



# Queue=FIFO:first in first out
# basic operation
# 1) Enqueue:Add a new element to the queue
# 2) Dequeue=remove & return the first(front) cleaned
# 3) peak=
# 4) size


# Queue=[]
# Queue.append("sintu")
# Queue.append("rishi")
# Queue.append("suman")
# Queue.append("halchal")
# print("Queue after pushing", Queue)
# # Pop (remove elements from top)
# front_element = Queue.pop(0)
# print("Popped element:", front_element)
# print("Queue after popping:", Queue)

# # Peek (check top element without removing)
# print("Top element is:", Queue[0])


# # creating class of queue
class Queue:
    def __init__(self):
        self.queue=[]

    def push(self,element):
        self.queue.append(element)

    def pop(self):
        if self.isEmpty():
            return "queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)


myQueue=Queue()
myQueue.push("azoo")
myQueue.push("halchal")
print("Queue elements now:", myQueue.queue)
print("Element popped:", myQueue.pop())
print("Front element now:", myQueue.peek())
print("Queue size:", myQueue.size())