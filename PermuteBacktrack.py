#backtracking to find all of the possible permutaion of the given string well 
# i have just encountred the backtracking algo that states that it moves to the specific
# condition and then terminates and get back to explore other possible methods 
# lets start 

res=[]

def permute(s,left,right):
    if(left==right):
        res.append(''.join(s))
        return;

    for i in range(left,right+1):
        s[left],s[i]=s[i],s[left]
        permute(s,left+1,right)
        #backtrack
        s[left],s[i]=s[i],s[left]
        

s="ABGS"
print(permute(list(s),0,len(s)-1))
print(res)
