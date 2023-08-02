# using DP to calculate if the number is reachable to the last index  or not 


def main(nums):
    n=len(nums)
    reach=0
    for i in range(0,n):
        if(i>reach):
            return 0
        reach=max(reach,i+nums[i])

        if(reach>=n-1):
            return 1
    
    return 0

if __name__=="__main__":
   print( main([2,3,1,1,4]))

