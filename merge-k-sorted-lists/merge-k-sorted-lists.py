# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        node_list = []
        sentinel = head = ListNode(0, None)
        
        for item in lists:
            while item:
                node_list.append(item.val)
                item = item.next
        
        for item in sorted(node_list):
            head.next = ListNode(item, None)
            head = head.next
        
        return sentinel.next    
        