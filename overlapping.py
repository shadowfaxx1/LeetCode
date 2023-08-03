#program to find if the sequence is overlapping or not 
# and if it is then return the count how manny to delete to find the correct solution 
#dynammic # greedy 
def comprator(ele1):
    return ele1[0]

def main(values):
    values= sorted(values,key=comprator)
    maxelementuptonow=values[0][1]
    print(values)
    c=0
    for i in range(1,len(values)-1):
        if values[i][0]<maxelementuptonow:
            c+=1
            maxelementuptonow=min(maxelementuptonow,values[i][1])
        else:
            maxelementuptonow=values[i][1]
    print(f"total number of elements to be removed {c} ")


if __name__=="__main__":
    main([[1,2],[2,3],[3,4],[1,3]])
