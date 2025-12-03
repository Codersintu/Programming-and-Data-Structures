def Binary_search(arr,target):
    left,right=0,len(arr)-1

    while left <=right:
        mid=(left+right)//2

        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            left=mid+1
        else:
            right=mid-1
    return -1


print(Binary_search([1,2,4,5,6,4,3,32,4],32))
        