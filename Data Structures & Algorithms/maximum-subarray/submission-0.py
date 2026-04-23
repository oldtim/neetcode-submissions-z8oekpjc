class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = nums[0]
        total_max = nums[0]
        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            total_max = max(total_max, curr_max)
    
        return total_max

        