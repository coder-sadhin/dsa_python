from stack_using_LL import Stack

# this operation are using for revarse an string using stack 
def reverse_string(string):
    s = Stack()
    for i in string:
        s.push(i)
    res = ""
    while (not s.is_empty()):
        res = res + s.pop()
    print(res)

# reverse_string("chokka")

# this operation are using for set string delete and undo and redo
def text_editor(text,pattern):
    u = Stack()
    r = Stack()

    for i in text:
        u.push(i)

    for i in pattern:
        if i == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)

    res = ""
    while(not u.is_empty()):
        res = u.pop() + res
    print(res) 

# text_editor("akkas","uurruuuur")

# this function for mathmetical expretion
def brackets(expr):
    s = Stack()
    for i in expr:
        if i == '(':
            s.push(i)
        elif i == ')':
            if s.peek() == '(':
                s.pop()
            else:
                print("Imbalanced")
                return 

    if (s.is_empty()):
        print("Balanced")
    else:
        print("Imbalanced")

# brackets("(a+b)")