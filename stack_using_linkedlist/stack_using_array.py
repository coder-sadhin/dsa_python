class Stack:
    def __init__(self,size):
        self.size = size
        self.__stack = [None] * self.size
        self.top = -1
    
    def push(self,value):
        if self.top == self.size - 1:
            return "Overflow"
        else:
            self.top+=1
            self.stack[self.top] = value