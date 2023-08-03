#so this problem requires us to solve it using dutch national flag algo 
# i also solved it using it using ordered_map but the TLE for large test cases got hit 

#firstly we need 3 points 
#we have target a and b to which we need to follow the partioning 

def swap(a,b):
    temp=a
    b=a
    a=temp


values =[ 2, 1, 3, 3, 4]
a=2
b=3

low=0
high=len(values)-1
mid=low

while(mid<=high):
    if(values[mid] < a ):
        values[mid],values[low]=values[low],values[mid]
        
        low+=1
        mid+=1
    elif(values[mid] > b):
        values[mid],values[high]=values[high],values[mid]
        high-=1
    else:
        mid+=1
    
print(values)


