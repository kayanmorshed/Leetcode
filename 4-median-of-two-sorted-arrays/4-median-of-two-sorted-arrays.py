class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_median(merged):
            if len(merged) % 2 == 1:
                return float(merged[len(merged)//2])
            else:
                return float((merged[len(merged)//2 - 1] + merged[len(merged)//2])/2)
        
        # determine median of the merged arrays
        m, n = len(nums1), len(nums2)
        if m == 0 and n == 0: return
        elif m == 0: return find_median(nums2)
        elif n == 0: return find_median(nums1)
        
        merged = []
        count = 0
        i, j = 0, 0
        flag_i, flag_j = 0, 0
        
        while count < m + n:
            if flag_i == 1 and flag_j == 0:
                merged.append(nums2[j])
                j += 1
            
            elif flag_i == 0 and flag_j == 1:
                merged.append(nums1[i])
                i += 1
            
            else:
                if nums1[i] <= nums2[j]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            
            count += 1
            
            if i == m: flag_i = 1
            if j == n: flag_j = 1
                
        # call the method find_median()
        return find_median(merged)
        