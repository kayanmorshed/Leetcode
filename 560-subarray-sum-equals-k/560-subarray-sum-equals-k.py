class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        collision_map = {0: 1}
        curr_sum, count = 0, 0
        
        for idx in range(len(nums)):
            curr_sum += nums[idx] # update the running sum
            
            # check whether the curr_sum along with a stored number  
            # in collision_map adds up to the desired number k
            if (curr_sum - k) in collision_map: 
                count += collision_map[curr_sum-k]
            
            # update the collision_map based on frequency
            if curr_sum in collision_map:
                collision_map[curr_sum] += 1
            else:
                collision_map[curr_sum] = 1
        
        return count
                