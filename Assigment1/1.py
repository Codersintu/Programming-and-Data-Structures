import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def parameter(self):
        return 2 * math.pi * self.radius
    
c = Circle(6)
print ("Area:", c.area())
print ("Parameter:", c.parameter())

# QNA2:
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None  

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self_size=0

    def Enqueue(self,data):
        new_node=Node(data)
        if self.rear is None:
            self.front=self.rear=new_node
            return
        self.rear.next=new_node
        self.rear=new_node

        
    
