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
    
    # this is for veiw the linked list
    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    
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

    # this is for append to the list
    # its called for append on tail
    def append(self,value):
        new_node = Node(value)

        # if list is empty
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return

        curr = self.head
        while curr.next != None:
            curr = curr.next

        # you are at the last node
        curr.next = new_node
        self.n = self.n + 1

    # this function for insert at any position of the list
    def insert_after(self,after,value):
        new_node = Node(value)
        curr = self.head

        # find the node of the index
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        # inserting the value
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return 'Item not found'
    


