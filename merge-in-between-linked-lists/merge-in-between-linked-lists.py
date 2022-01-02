# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        sentinel = ListNode('#', list1)
        
        idx, prev = 1, None
        last_segment = None
        while list1:
            prev = list1
            if idx == a:
                while idx <= b:
                    list1 = list1.next
                    idx += 1
                
                last_segment = list1.next
                prev.next = list2
                list1 = prev.next
            else:
                list1 = list1.next
                idx += 1

        prev.next = last_segment
        
        return sentinel.next