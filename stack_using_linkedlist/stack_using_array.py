class Stack:
    def __init__(self,size):
        self.size = size
        self.__stack = [None] * self.size
        self.top = -1