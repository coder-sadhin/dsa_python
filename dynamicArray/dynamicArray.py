import ctypes
# using datatypes of c proggramming language
class MyArray:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type ka array with size -> self.size
        self.A = self.__make_array(self.size)

    # this function for showing the lenth
    def __len__(self):
        return self.n
    
    # this for print
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'

    # this function are use for append a value on last of the list
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        self.A[self.n] = item
        self.n += 1
    
    # this function are use for delete an value from last of the list
    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n = self.n - 1

    # this function are use for clear the list
    def clear(self):
        self.n = 0
        self.size = 1

    # this function are using for find a index number from the list
    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'ValueError - not in list'

    # this function are use for insert a value on specific position on this array
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    # this function use for delete value from the list
    def remove(self,item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos

    # this function use for crate a new array
    def __resize(self,new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of old array to new one
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    # this function use for get item, using like list []
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'IndexError'

    # this function use for delete value form position
    def __delitem__(self,pos):
        if 0<= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
        self.n = self.n - 1

    def __make_array(self,capacity):
        # referential array(C type)
        return (capacity*ctypes.py_object)()
    

Lst=MyArray()

Lst.append(1)
Lst.append('hello')
Lst.append(False)
Lst.append(4.5)

print(Lst)
Lst.remove(4.5)
print(Lst)
