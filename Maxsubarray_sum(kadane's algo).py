
#kadane's algo to find the largest subarray sum 

def kadane(li,n)->int:
    maxsum=li[0]
    max_sofar=li[0]
    for i in range(1,n):
        maxsum=max(maxsum+li[i],li[i])
        max_sofar=max(maxsum,max_sofar)

    return max_sofar

def main():
    ls=     [-2,1,-3,4,-1,2,1,-5,4]
    ls_s = ' '.join(map(str, ls))
    print(ls_s)
    li = list(map(int,input().split()))
    print("maxSum=",kadane(li,len(li)))
    
if __name__ =="__main__":
    main()

