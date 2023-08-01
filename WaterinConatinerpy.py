# used two pointer approach in this 


def watercon(li,n):
    i=0
    j=n-1
    maxarea=0
    while (i<j):
        area=min(li[i],li[j])*(j-i)
        maxarea=max(maxarea,area)
        if(li[i]<li[j]):
            i+=1
        else:
            j-=1
    return maxarea
def main():
    li= [1,8,6,2,5,4,8,3,7]
    li_str=' '.join(map(str,li))
    print(li_str)
    inp=list(map(int,input().split()))
    print(watercon(inp,len(inp)))


if __name__=="__main__":
    main()
