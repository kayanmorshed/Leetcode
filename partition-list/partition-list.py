# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        
        sentinel_left = left_list = ListNode('#')
        sentinel_right = right_list = ListNode('#')
        
        while head:
            if head.val < x:
                left_list.next = head
                left_list = left_list.next
            
            else:
                right_list.next = head
                right_list = right_list.next
            
            # advance the head position
            head = head.next
        
        right_list.next = None
        left_list.next = sentinel_right.next
        return sentinel_left.next