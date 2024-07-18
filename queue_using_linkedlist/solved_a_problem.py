from queue_using_linkedlist import Queue

def check_balanced_parenthesis(s):
    stk = Queue()
    # for itm in s:
        # print(itm)
    for item in s:
        print(item)
        if item in '({[':
            stk.enqueue(item)  # Use push instead of enqueue
        elif item in ')}]':
            if stk.is_empty():
                return False
            if item == ')' and stk.front_item() == '(':  # Use front_item instead of front_item
                stk.dequeue()  # Use dequeue instead of dequeue
            elif item == '}' and stk.front_item() == '{':
                stk.dequeue()
            elif item == ']' and stk.front_item() == '[':
                stk.dequeue()
            else:
                return False
    #     print(item)
    #     if item == '(':
    #         stk.enqueue(item)
    #     elif item == '{':
    #         stk.enqueue(item)
    #     elif item == '[':
    #         stk.enqueue(item)
    #     elif item == ')':
    #         if stk.front_item() == '(':
    #             stk.dequeue()
    #         else:
    #             return False
    #     elif item == '}':
    #         if stk.front_item() == '{':
    #             stk.dequeue()
    #         else:
    #             return False
    #     elif item == ']':
    #         if stk.front_item() == '[':
    #             stk.dequeue()
    #         else:
    #             return False
    #     elif item == ' ':
    #         continue
    #     else:
    #         continue
            
    return stk.is_empty()

s="{[(a+b) + (c+d)]}"

print(check_balanced_parenthesis(s))