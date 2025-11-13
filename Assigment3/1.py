def isIdentical(a,b):
    if a is None and b is None:
        return True
    
    if a is not None and b is not None:
        return False
    
    if a.value != b.value:
        return False
    

    return isIdentical(a.left,b.left) and isIdentical(a.right,b.right)


    
