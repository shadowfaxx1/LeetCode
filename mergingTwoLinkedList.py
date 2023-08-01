# merging 2 sorted linked list using merge sort merging function 

class Node:
    def __init__(self, data=0,next=None):
        self.data = data
        self.next = None

class solution(object):
    def __init__(self,list1=None,list2=None) -> None:
        self.list1=list1
        self.list2=list2

    def merge(self,list1, list2):
        ptr1=list1
        ptr2=list2
        head=Node(0)
        tail=head

        while(ptr1 and ptr2):
            if(ptr1.data<=ptr2.data):
                head.next=Node(ptr1.data)
                ptr1=ptr1.next
            else:
                head.next=Node(ptr2.data)
                ptr2=ptr2.next
            head=head.next
        
        while(ptr1):
            head.next=Node(ptr1.data)
            ptr1=ptr1.next
            head=head.next
        while(ptr2):
            head.next=Node(ptr2.data)
            ptr2=ptr2.next
            head=head.next

        return tail.next
        
    def mergeTwoLists(self, list1, list2):
        return self.merge(list1,list2)
    
    def createLinkedList(self, values):
        # Function to create a linked list from a list of values
        if not values:
            return None
        head = Node(values[0])
        curr = head
        for val in values[1:]:
            curr.next = Node(val)
            curr = curr.next
        return head

    def mergeLinkedLists(self, values1, values2):
        # Function to merge two linked lists created from given values
        list1 = self.createLinkedList(values1)
        list2 = self.createLinkedList(values2)
        return self.mergeTwoLists(list1, list2)
    
def main():
    # Create a Solution object
    sol = solution()

    # Example 1: Merge two linked lists directly
    list1 = sol.createLinkedList([1, 3, 5])
    list2 = sol.createLinkedList([2, 4, 6])
    merged_list = sol.mergeTwoLists(list1, list2)

    # Print the merged linked list
    print("Merged List (Example 1):")
    curr = merged_list
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

    # Example 2: Merge two lists of values using mergeLinkedLists
    values1 = [1, 3, 5]
    values2 = [2, 4, 6]
    merged_list = sol.mergeLinkedLists(values1, values2)

    # Print the merged linked list
    print("\nMerged List (Example 2):")
    curr = merged_list
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

if __name__ == "__main__":
    main()
