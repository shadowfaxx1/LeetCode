
def binarysearch(arr):
    left=0
    right=len(arr)-1

    while(left<right):
        mid=left+(right-left)//2
        if(arr[mid] < arr[right] ):
            right = mid
        else:
            left=mid+1

    return arr[left]



arr=[3,4,5,1,2]

z=binarysearch(arr)
print(z)

