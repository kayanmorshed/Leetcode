# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = l3 = ListNode(0)
        # l3 = *root
        
        while l1 or l2:
            if l1 and not l2: # if l2 doesn't exist
                sum_ = (l1.val + carry)%10
                carry = (l1.val + carry)//10
                l1 = l1.next
            elif not l1 and l2: # if l1 doesn't exist
                sum_ = (l2.val + carry)%10
                carry = (l2.val + carry)//10
                l2 = l2.next
            else: # if both l1 and l2 exist
                sum_ = (l1.val + l2.val + carry)%10
                carry = (l1.val + l2.val + carry)//10
                l1 = l1.next
                l2 = l2.next
                
            # create the output linked list
            l3.next = ListNode(sum_)
            # print(l3.next.val)
            l3 = l3.next
            
            # check whether both linked list is None and only there is carry
            if not l1 and not l2 and carry > 0:
                l3.next = ListNode(carry)
                break
        
        return root.next
                
        