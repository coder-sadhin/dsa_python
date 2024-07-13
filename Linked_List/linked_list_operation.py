class Node:
  def __init__(self,value):
    self.data = value
    self.next = None

class LinkedList:
    # this is linked list constractor
    def __init__(self):
        # Empty Linked List
        self.head = None
        # no of nodes in the LL
        self.n = 0

    # this is for showing len of the list
    def __len__(self):
        return self.n
    
    # this is for insert value on head 
    def insert_head(self,value):
        # new node
        new_node = Node(value)
        # create connection
        new_node.next = self.head
        # reassign head
        self.head = new_node
        # increment n
        self.n = self.n + 1


