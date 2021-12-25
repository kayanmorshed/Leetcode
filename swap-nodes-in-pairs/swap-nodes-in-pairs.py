# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        
        sentinel = root = ListNode('#')
        
        tempNode = None
        count = 0
        
        while head:
            count += 1
            
            if count == 2:
                tempNode.next = head.next
                head.next = tempNode

                root.next = head
                root = root.next.next
                
                head = tempNode.next
                
                tempNode = None
                count = 0
            
            else:
                tempNode = head 
                head = head.next
        
        return sentinel.next