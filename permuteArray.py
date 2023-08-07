#backtracking is not neccesarily importatnt so we stick to the main function calling 
res=[]
def permute(vec,left,right):
    if(left==right):
        res.append(vec[:])
        return ;
    
    for i in range(left,right+1):
        vec[i],vec[left]=vec[left],vec[i] #swaping
        permute(vec,left+1,right)

vec=[1,2,3]
permute(vec,0,len(vec)-1)
print(res)

#      Call permute([1, 2, 3], 0, 2)
#         vec=[1, 2, 3], left=0, right=2

#            /          |          \
#      swap 1, 1    swap 1, 2    swap 1, 3
#          /            |            \
# Call permute([1, 2, 3], 1, 2)   Call permute([1, 3, 2], 1, 2)   Call permute([1, 3, 2], 2, 2)
#         vec=[1, 2, 3], left=1, right=2      vec=[1, 3, 2], left=1, right=2       vec=[1, 3, 2], left=2, right=2

#           |              |              |
#     swap 2, 2     swap 2, 2    swap 2, 2
#          |              |              |
# Call permute([1, 2, 3], 2, 2)   Call permute([1, 3, 2], 2, 2)   Call permute([1, 3, 2], 2, 2)
#         vec=[1, 2, 3], left=2, right=2      vec=[1, 3, 2], left=2, right=2       vec=[1, 3, 2], left=2, right=2

#             ... (no more swaps) ...
#            /          |          \
# Call permute([2, 1, 3], 1, 2)   Call permute([2, 3, 1], 1, 2)   Call permute([2, 3, 1], 2, 2)
#         vec=[2, 1, 3], left=1, right=2      vec=[2, 3, 1], left=1, right=2       vec=[2, 3, 1], left=2, right=2

#             ... (no more swaps) ...
#            /          |          \
# Call permute([3, 2, 1], 1, 2)   Call permute([3, 1, 2], 1, 2)   Call permute([3, 1, 2], 2, 2)
#         vec=[3, 2, 1], left=1, right=2      vec=[3, 1, 2], left=1, right=2       vec=[3, 1, 2], left=2, right=2

#             ... (no more swaps) ...
