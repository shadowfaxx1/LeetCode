class Node:
    def __init__(self, value=None,next=None):
        self.value=value
        self.next=next

    
class solution(object):
    def __init__(self,l1) -> None:
        self.l1=l1

    def createNode(self):
        li=self.l1
        head= Node(li[0])
        temp= head
        for i in li[1:]:
            temp.next= Node(i)
            temp=temp.next;
        
        return head
    def deleteNthNodeFromlast(self,root,n):
        dummy =Node()
        dummy.next=root
        fast=dummy
        slow=dummy

        for i in range(0,n+1):
            if not fast:
                return root
            fast=fast.next
        
        while (fast!=None ):
            slow=slow.next
            fast=fast.next
        
        todelete= slow.next
        slow.next=todelete.next
        del todelete

        newhead=root.next
        del dummy

        return newhead

s=solution([1,2,3,4,5,7])

root=s.createNode()
dummy=root
while(root):
    print(root.value,end="->")
    root=root.next

print("after")
head=s.deleteNthNodeFromlast(dummy,1)

while(head):
    print(head.value,end="->")
    head=head.next


