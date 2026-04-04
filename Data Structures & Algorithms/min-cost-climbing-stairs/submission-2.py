class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        min_1st = cost[0]
        min_2nd = cost[1]
        # if len(cost) < 3:
        #     return min(min_2nd, min_1st)
        for i in range(2,len(cost)):
            temp = min_2nd
            min_2nd = min(min_1st, min_2nd) + cost[i]
            min_1st = temp
        return min(min_2nd, min_1st)

#第一次寫沒過，後來檢視原來是題目看錯，是要走超過最後一位cost[-1]
#，而非走到最後一位cost[-1]



        