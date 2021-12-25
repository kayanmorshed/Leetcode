# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        temp_sentinel = ListNode('#')
        counter = 1
        prev = None
        given_left = left
        while head:
            
            # we encountered the left positioned node
            if counter == left:
                temp_node_list = []
                
                while left <= right:
                    temp_node_list.append(head.val)
                    head = head.next
                    left += 1
                
                reversed_list = temp_node_list[::-1]
                node = ListNode(reversed_list[0], None)
                temp_sentinel.next = node
                
                for i in range(1, len(reversed_list)) :
                    node.next = ListNode(reversed_list[i], None)
                    node = node.next
                
                if given_left > 1:
                    prev.next = temp_sentinel.next
                else:
                    node.next = head
                    return temp_sentinel.next
                
                node.next = head
                return sentinel.next
            
            else:
                prev = head
                head = head.next
                counter += 1
        