class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        cost[i] = cost of ith step
        pay and take 1 or 2 steps
        start: 0, 1
        obj: minimum cost to reach the top
        
        cost[0] = 10
        cost[1] = 15
        cost[2] = min(cost[2-1] + cost[2], cost[2-2] + cost[2])
        
        cost[0] = 1
        cost[1] = 100
        cost[2] = min(cost[0] + cost[2], cost[1] + cost[2]) = 2
        cost[3] = min(cost[2] + cost[3], cost[1] + cost[3]) = 3
        
        '''
        
        if len(cost) == 2: return min(cost[0], cost[1])
        
        for i in range(2, len(cost)):
            cost[i] = min(cost[i-2] + cost[i], cost[i-1] + cost[i])
        
        return min(cost[len(cost)-2], cost[len(cost)-1])
        