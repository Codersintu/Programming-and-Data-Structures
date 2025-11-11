# 29-10-2025

# list=[1,2,3,4,5]
# search_value=3

# if search_value in list:
#     print(list.index(search_value))
# else:
#     print("not found")

# Binary Search:
# it search through a started array/list

def binary_search(arr,target):
    low=0
    high=len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid +1
        else:
            high= mid - 1
    return -1

arr=[1,2,4,5,6,7,8,9]
target=7
result = binary_search(arr, target)
print(result)

