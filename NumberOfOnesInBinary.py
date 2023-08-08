


#we have a number we need to identify the how many one's are occuring in the binary up till the Nth 
#number so lets just put this way 
# for N = 4
# 0 - > 0
# 1 - > 1
# 2 -> 10
# 3->  11
# 4 -> 100
# so if we count the one's it comes out to be [0,1,1,2,1]
#solving using dynamic programming 




num= 5
n=num+1
dp=[0]*n

offset=1

for i in range(1,num+1):
    if(offset*2==i):
        offset*=2
    dp[i]=dp[i-offset]+1
print(dp)




