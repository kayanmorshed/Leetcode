# hep from this solution: https://leetcode.com/problems/house-robber-ii/discuss/893957/Python-Just-use-House-Robber-twice

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        # call the helper method for nums[2:len(nums)-1]
        # add the returned value with nums[0]
        # we skip the item nums[1] since we considered that nums[0] has been counted
        money_in_first_pass = nums[0] + self.helper(nums[2:len(nums)-1])
        
        # call the helper method for nums[1:len(nums)]
        # we skip the item nums[0] since we considered that nums[-1] has been counted
        money_in_second_pass = self.helper(nums[1:len(nums)])
        
        return max(money_in_first_pass, money_in_second_pass)
        
    def helper(self, nums):
        dp1, dp2 = 0, 0
        
        for i in range(len(nums)):
            # update the sliding window
            # dp1 = dp2
            # dp2 = max(dp2, nums[i] + dp1)
            dp1, dp2 = dp2, max(dp2, nums[i] + dp1)
        
        return dp2
                
        