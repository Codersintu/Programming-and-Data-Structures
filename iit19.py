# hash function
# folding function

def folding_hash(key):
    key_str=str(key)
    total=0

    for i in range(0,len(key_str),2):
        part=int(key_str[i:i+2])
        total += part

    hash_value=total % 100
    return hash_value


keys=[123456,3455654356,23456332]
for k in keys:
    print(f"key {k} -> Hash value: {folding_hash(k)}")



# Mid_Square Method
def mid_square_hash(key):
    square=key * key
    square_str=str(square)
    mid=len(square_str) // 2

    middle_digits=square_str[mid-1:mid+1]
    hash_value=int(middle_digits)
    return hash_value % 100

keys=[12,23,45,67,89]
for k in keys:
    print(f"key {k} -> Hash value: {mid_square_hash(k)}")