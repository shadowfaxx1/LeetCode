



def max_sub(s,k):
    left=0
    right=len(s)-1
    max_length=0
    count=0
    mp={}
    while(right<len(s)-1):
        mp[s[right]]+=1
        count=max(count,mp[right])

        if((right-left+1) - count > k ):
            mp[s[left]]-=1
            left+=1
        max_length=max(max_length,right-left+1)
    print(mp)
    return max_length


s= " AABBAAB"
k=2
z=max_sub(s,k)
print(z)