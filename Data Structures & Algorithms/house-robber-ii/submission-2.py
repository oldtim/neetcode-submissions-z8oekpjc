class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp1 = [-1]*(len(nums)-1)
        dp2 = [-1]*(len(nums)-1)
        dp1[0] = nums[1]
        dp1[1] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp1[i-1] = max(nums[i]+dp1[i-3], dp1[i-2])
        
        dp2[0] = nums[0]
        dp2[1] = max(nums[0], nums[1])
        for j in range(2, len(nums)-1):
            dp2[j] = max(nums[j]+dp2[j-2], dp2[j-1])
        
        return max(dp1[-1], dp2[-1])



        