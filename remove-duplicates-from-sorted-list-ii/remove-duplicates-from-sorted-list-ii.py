# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode('#')
        sentinel.next = node = head
        node = head
        
        node_values = {}
        
        prev = None
        while head:
            if head.val not in node_values:
                node_values[head.val] = 1
                prev = head
                head = head.next
    
            else:
                node_values[head.val] += 1
                prev.next = head.next
                head = head.next
        
        node_values_list = list(node_values)
        
        # sentinel = prev = ListNode('#')
        prev = None
        while node:
            if node.val == node_values_list[0] and node_values[node_values_list[0]] > 1:
                node = node.next
                sentinel.next = node
                node_values_list.pop(0)
            
            elif node_values[node.val] > 1:
                prev.next = node.next
                node = node.next
            
            else:
                prev = node
                node = node.next
        
        return sentinel.next