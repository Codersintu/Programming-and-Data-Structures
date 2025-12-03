# 13-11-2025
# searching an element in an array using linear search
def linear_search(arr,key):
    count=0
    for i in range(len(arr)):
        if arr[i]==key:
            count+=1
            return i,count
    return -1

print("Element found at index:", linear_search([5,2,7,9,1],9))

def binary_search(arr,key):
    low,high=0,len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1


print("Element found at index:", binary_search([3, 5, 8, 12, 20, 25],12))


# Bubble sort
def bubble_sort(arr):
    n=len(arr)

    for i in range(n-1):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print("Sorted array is:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))


# selection sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort(["Priya", "Anusha", "zoya", "mona", "asha","sintu","halchal"]))
