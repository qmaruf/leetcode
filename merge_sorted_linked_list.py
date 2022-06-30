# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = list1
        curr2 = list2     
        
        if curr1 is None:
            return curr2
        
        if curr2 is None:
            return curr1
        
        if curr1.val <= curr2.val:
            head = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next
        
        curr = head
            
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1                
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
            
        if curr1:
            curr.next = curr1
        else:
            curr.next = curr2
        
        return head      
