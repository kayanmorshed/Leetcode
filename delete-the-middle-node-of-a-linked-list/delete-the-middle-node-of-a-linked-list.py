# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        if not head.next.next: 
            head.next = None
            return head
        
        # mid = -1
        count = 0
        sentinel = ListNode(0, head)
        
        while head:
            count += 1
            head = head.next
        
        mid = count // 2
        i = 0
        
        node = sentinel.next
        prev = None
        
        while i < mid:
            prev = node
            node = node.next
            i += 1
        
        prev.next = node.next
        
        return sentinel.next
        
        
        