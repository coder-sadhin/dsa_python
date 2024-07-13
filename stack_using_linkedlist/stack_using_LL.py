class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
     

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    