class Solution:
    def minPartitions(self, n: str) -> int:
        max_ = 0
        for digit in n:
            max_ = max(int(digit), max_)
        return max_  
        