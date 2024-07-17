class Node:
  def __init__(self,value):
    self.data = value
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None

q = Queue()