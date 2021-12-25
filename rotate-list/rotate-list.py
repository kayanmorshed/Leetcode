# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        
        sentinel = ListNode('#')  
        sentinel.next = head
        rotation = 1
        
        # method rootateRight        
        while rotation <= k:
            tempNode = head
            # get the 2nd last and the last node of the linked list
            second_last, last = self.getLastNodes(head)
            
            # rotate operation
            last.next = tempNode
            second_last.next = None
            
            # assign the rotated linked list into head for further rotation 
            head = last
            
            # check whether the current rotated linked list is te original linked list
            if sentinel.next == head:
                # cyclic operation
                if k % rotation == 0:
                    return head
                else:
                    k = k % rotation
                    rotation = 0
                
            rotation += 1
        
        return head
    
            
    def getLastNodes(self, node):
        second_last, last = None, node

        while node.next:
            second_last, last = node, node.next
            node = node.next

        return second_last, last
