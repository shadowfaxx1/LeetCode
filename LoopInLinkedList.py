# detecting loop using two pointers approach 
# slow pointer and fast pointer if the pointer meet then loop otherwise no loop 


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution(object):
    def __init__(self,li) -> list:
        self.li=li
        super().__init__()

    def makelinkedlist(self):
        li=self.li
        if not li:
            return None
        root=ListNode(li[0])
        curr=root
        for i in li[1:]:
            curr.next=ListNode(i)
            if(i==1):
                pointing=curr
            curr=curr.next
        curr.next=pointing
        return root
    def detetloop(self,root):

        slwptr=root
        fstptr=root
        if root==None:
            return 0
        
        while(fstptr!=None and fstptr.next!=None):
            print('slw',slwptr.val,'fst',fstptr.val)
            slwptr=slwptr.next
            fstptr=fstptr.next.next
            if(slwptr==fstptr):
                return 1
        return 0

s=solution([3,2,3,1,4,5])
root=s.makelinkedlist()

bool=s.detetloop(root)

print(bool)

# print("Merged List (Example 1):")
# curr = list1
# while curr:
#     print(curr.val, end=" -> ")
#     curr = curr.next
# print("None")
