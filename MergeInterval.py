


def comprator(ele):
    return ele[0]

def Merger(arr):
    arr=sorted(arr,key=comprator)
    i=0
    n=len(arr)
    vec=[]
    while i < len(arr):
        start= arr[i][0]
        end = arr[i][1]

        while i < n-1 and end>=arr[i+1][0]:
            end=max(end,arr[i+1][1])
            i+=1
        vec.append({start,end})
    print(vec)





arr= [ [1,3], [2,5] ,[8,10],[12,14]]
Merger(arr)

