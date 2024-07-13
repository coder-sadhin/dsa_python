class Node:
  def __init__(self,value):
    self.data = value
    self.next = None

class LinkedList:
  def __init__(self):
    # Empty Linked List
    self.head = None
    # no of nodes in the LL
    self.n = 0