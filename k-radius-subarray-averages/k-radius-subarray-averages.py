class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        length = len(nums)
        avgs = [-1] * length
        
        if length < (2 * k) +1:
            return avgs

        
        # for k index
        temp = nums[0 : (2*k)+1]
        div = len(temp)
        sum_ = sum(temp)
        avgs[k] = sum_//div
        
        i = k+1
        while i < length-k:
            sum_ = sum_ - nums[i-k-1] + nums[i+k]
            avgs[i] = sum_//div
            
            i += 1
        
        return avgs
        