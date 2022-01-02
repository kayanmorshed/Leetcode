# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.node_list = []
        
        while head:
            self.node_list.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        pick = int(random.random() * len(self.node_list))
        return self.node_list[pick]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()