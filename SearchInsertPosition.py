#python function to search for the insert position in the sorted array 
# i used lower_bound in the c++ program 
# using it with distance function gives you the exact info 


import bisect 
def binarySearch(arr, target):
    return bisect.bisect_left(arr,target)

arr= [1,3,5,6]
t=5

print(
binarySearch(arr,t))
                 

