class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums_count = Counter(nums)
        
        while True:
            curr = []
            for item in res:
                for num in nums:
                    temp = item + [num]
                    temp_count = Counter(temp)
                    flag = 0
                    
                    for key in temp_count:
                        if temp_count[key] > nums_count[key]:
                            flag = 1
                            break
                    
                    if flag == 0 and temp not in curr:
                        curr.append(temp)

            res = curr
            if len(res[0]) == len(nums):
                break
            
        return res
        