class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = {}
        
        for item in points:
            curr_dist_sqr = item[0] ** 2 + item[1] ** 2
            if curr_dist_sqr not in distance:
                distance[curr_dist_sqr] = [item]
            else:
                distance[curr_dist_sqr].append(item)
        
        res = []
        i = 0
        
        for key in sorted(distance.keys()):
            kval = distance[key]
            
            if len(kval) > 1:
                for item in kval:
                    res.append(item)
                i += len(kval)
            else:
                res.append(kval[0])
                i += 1
            
            if i >= k:
                break
        
        return res[0:k]
            
        