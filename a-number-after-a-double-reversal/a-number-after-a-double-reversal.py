class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev_1 = int(str(num)[::-1])
        return num == int(str(rev_1)[::-1])
        
        