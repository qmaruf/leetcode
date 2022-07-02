# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        
        if head.next is None:            
            return head
        
        if head.next.next is None:
            return head.next
        
        slow = head
        fast = head
        
        jump = 0
        while head:
            head = head.next
            if head:
                jump += 1
                if head.next:
                    head = head.next
                    jump += 1
                    slow = slow.next
        
        if jump&1 == 1:
            slow = slow.next
        
        return slow
        
        
