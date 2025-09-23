def delete_middle(stack, current=0):
    n = len(stack)

    if current == n // 2:
        stack.pop()   
        return
    
    x = stack.pop()
    delete_middle(stack, current + 1)
    stack.append(x)



stack = [10, 20, 30, 40, 50]  
delete_middle(stack)
print("After deleting middle:", stack)
