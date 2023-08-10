

class Node:
    def __init__(self, data=None,next=None)->None:
        self.data=data
        self.next=next

class solution(object):
    def createLinkedList(self,v1):
        if not v1:
            return None;
        root=Node(v1[0])
        head=root
        for i in v1[1:]:
            head.next=Node(i)
            head=head.next
        return root
    def addingtwoLinkedlist(self,l1,l2):
        s1=[]
        s2=[]
        while(l1):
            s1.append(l1.data)
            l1=l1.next
        while(l2):
            s2.append(l2.data)
            l2=l2.next
        
        head=Node(None)

        carry=0
        while(s1 or s2 or carry>0):
            sum=carry
            if(s1):
                sum+=int(s1.pop())
            if(s2):
                sum+=int(s2.pop())
            carry=sum//10
            sum=sum%10
            temp = Node(sum)
            temp.next=head
            head=temp

        return head
    
obj=solution()
lx=    [1]
lz= [9,9]
l1=obj.createLinkedList(lx)
l2=obj.createLinkedList(lz)
x=obj.addingtwoLinkedlist(l1,l2)

while x :
    print(x.data)
    x=x.next




            
    


