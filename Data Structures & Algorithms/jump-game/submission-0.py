class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]+i >= goal:
                goal = i
        
        return True if goal == 0 else False
            








# 想了一下但最後還是看hint，hint中解法，可以藉由只更新一個更小的goal成立，是因為array中存的是max step
#，如果能夠到達更大的goal的前一個step，一定可以到達更小的goal。所以不會漏算可能的step路徑
#，比如nums[-5]=4；nums[-3]=2，是跳到nums[-1]的兩個路徑，此時更新goal從-3到-5只會讓可能性更多，因為能跳到-3的一定能跳到-5，反之則否
