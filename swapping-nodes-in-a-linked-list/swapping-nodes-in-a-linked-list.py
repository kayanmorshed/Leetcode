# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        
        if head.next and not head.next.next:
            temp = head
            new_head = head.next
            new_head.next = temp
            temp.next = None
            return new_head
        
        sentinel = ListNode('#', head)
        node_list = []
        
        prev, idx = None, 1
        while head:
            if idx == k-1:
                prev = head
            node_list.append(head.val)
            head = head.next
            idx += 1
        
        length = idx-1
        node = sentinel.next
        prev_k, idx = None, 1
        while node:
            if idx == length - k:
                prev_k = node
            node = node.next
            idx += 1
        
        # special case: k == 1    
        if k == 1 or k == length:
            if k == length:
                temp = prev_k
                prev_k = prev
                prev = prev_k

            second_node = sentinel.next.next
            first_node = ListNode(node_list[len(node_list)-1], second_node)
            last_node = ListNode(node_list[0], None)
            prev_k.next = last_node
            return first_node            
        
        elif prev.next == prev_k or prev_k.next == prev:
            if prev_k.next == prev:
                temp = prev_k
                prev_k = prev
                prev = temp
            
            first_to_replace, second_to_replace = prev.next, prev_k.next
            temp_replace = second_to_replace
            first_to_replace.next = second_to_replace.next
            prev.next = temp_replace
            temp_replace.next = first_to_replace
            return sentinel.next
            
        else:
            first_replacement = prev_k.next
            first_replacement_after = prev.next.next
            second_replacement= prev.next
            second_replacement_after = prev_k.next.next

            prev.next = first_replacement
            first_replacement.next = first_replacement_after
            
            prev_k.next = second_replacement
            second_replacement.next = second_replacement_after
        
            return sentinel.next
            
        