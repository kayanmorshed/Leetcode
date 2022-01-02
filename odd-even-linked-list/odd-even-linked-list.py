# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        if not head.next:
            return head
        
        sentinel = ListNode('#', head)
        odd_end = head
        even_start = head.next
        even_end = even_start
        
        while even_end.next and even_end.next.next:
            third = even_end.next
            fourth = third.next
            
            odd_end.next = third
            # reset odd pointer
            odd_end = third
            
            third.next = even_start
            even_end.next = fourth
            # reset even
            even_end = fourth
        
        if even_end.next:
            odd_end.next = even_end.next
            odd_end.next.next = even_start
            even_end.next = None
            
            
        return sentinel.next