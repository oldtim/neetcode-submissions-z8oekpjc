class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        min_1st = cost[0]
        min_2nd = cost[1]
        if len(cost) < 3:
            min(min_2nd, min_1st)
        for i in range(2,len(cost)):
            temp = min_2nd
            min_2nd = min(min_1st, min_2nd) + cost[i]
            min_1st = temp
        return min(min_2nd, min_1st)



        