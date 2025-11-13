# 11/11/2025

# Divide
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    

    mid=len(arr) //2
    left_half=arr[:mid]
    right_half=arr[mid:]


    left_sorted=merge_sort(left_half)
    right_sorted=merge_sort(right_half)


    return merge(left_sorted,right_sorted)




# conquer and merge
def merge(left,right):
    result=[]
    i=j=0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr=[11,16,3,24,46,22,7]
print("Original array",arr)
print("sorted array",merge_sort(arr))