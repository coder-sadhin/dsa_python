# this is for class declaretion
class Node:
  def __init__(self,value):
    self.data = value
    self.next = None

# decliar some example
a = Node(1)
b = Node(2)
c = Node(3)

# this is how to link on list
a.next = b
b.next = c

