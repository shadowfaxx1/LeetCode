# this uses sliding window approach to get the min length of the target
#sum in the array 


def slidingwindow(li,n , target)->int:
    left=0
    right=0
    getsum=li[0]
    mini=999999999
    while(right<n):
        if(getsum<target):
            right+=1
            if(right<n):
                getsum+=li[right]
        if(getsum>=target):
            mini=min(mini,right-left+1)
            getsum-=li[left]
            left+=1

    if(mini ==999999999):
        return 0
    return mini


def main():
    ar=[2,3,1,2,4,3]
    print(slidingwindow(ar,len(ar),7))

if __name__=="__main__":
    main()