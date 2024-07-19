class Stack:
    def __init__(self, size):
        self.size = size
        self.__stack = [None] * self.size
        self.top = -1
    
    def push(self, value):
        if self.top == self.size - 1:
            return False  # Stack is full
        self.top += 1
        self.__stack[self.top] = value
        return True  # Successfully pushed
        
    def pop(self):
        if self.top == -1:
            return None  # Stack is empty
        data = self.__stack[self.top]
        self.top -= 1
        return data


    def traverse(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            for i in range(self.top + 1):
                print(self.__stack[i], end=' ')
            print()  # Add a newline after traversal

# Test the stack
s = Stack(3)
print(s.push(4))  # True
print(s.push(5))  # True
print(s.push(6))  # True
print(s.push(7))  # False (overflow)
s.traverse()  # Stack is empty
print(s.pop())  # 6
print(s.pop())  # 5
print(s.pop())  # 4
print(s.pop())  # None (empty)

s.traverse()  # Stack is empty