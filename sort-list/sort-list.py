# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next
        
        sorted_list = sorted(node_list)
        
        node = ListNode(sorted_list[0], None)
        sentinel = ListNode(0, node)
        
        for i in range(1, len(sorted_list)):
            node.next = ListNode(sorted_list[i], None)
            node = node.next
        
        return sentinel.next