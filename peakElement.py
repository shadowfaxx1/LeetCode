#so we need to find the peak element which is greater than all its neightbors ok 
# so we implement a binary search function and get the peak elemetn 



arr=[1, 2, 1, 3, 5, 6, 4]
right=len(arr)-1
left=0

while left < right:
    mid=left+(right-left)//2
    if arr[mid]<arr[mid+1]:
        left=mid+1
    else:
        right=mid

print(left)

    