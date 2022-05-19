# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        
        # keep track of head.next.next before swappinh
        temp = head.next.next
        
        # swap head with head.next
        head, head.next = head.next, head
    
        # recursive call
        head.next.next = self.swapPairs(temp)
        
        return head