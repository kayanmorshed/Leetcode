# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        sentinel = ListNode(0, head)
        
        counter = 0
        while head:
            counter += 1
            head = head.next
        
        if counter == n: return sentinel.next.next
        
        node = sentinel.next
        i = 0
        while node:
            i += 1
            if i == counter - n:
                node.next = node.next.next
                break
            node = node.next
                
        return sentinel.next