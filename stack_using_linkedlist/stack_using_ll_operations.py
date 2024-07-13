from stack_using_LL import Stack

def reverse_string(string):
    s = Stack()
    for i in string:
        s.push(i)
    res = ""
    while (not s.is_empty()):
        res = res + s.pop()
    print(res)
    
reverse_string("chokka")