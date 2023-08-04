


class nodes():
    def __init__(self,data=None,next=None) -> None:
        self.data= data
        self.next=next


class solution(object):

    def __init__(self,li) -> None:
        self.li=li
    def create(self):
        values=self.li
        head =nodes(values[0])
        curr =head
        for i in values[1:]:
            curr.next=nodes(i)
            curr=curr.next
        return head
     
    def cout(self,root):
        while root!=None :
            print(root.data,end=" ")
            root=root.next
    def reverse(self,root):
        prev_node=None
        curr_node=root
        next_node=None
        while(curr_node!=None):
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node
        root=prev_node
        return root
    

s=solution([1,2,3,4,5])
root=s.create()
print("before reversing")  # before reversing
s.cout(root)
print()
print("after reversing")  # before reversing

root1=s.reverse(root)
s.cout(root1)








