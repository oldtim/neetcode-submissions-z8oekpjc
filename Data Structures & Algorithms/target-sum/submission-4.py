class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = 0
        for n in nums:
            total += n
        if total < abs(target) or ((total-abs(target))%2) != 0:  #補丁:abs()
            return 0

        half = (total-abs(target))//2    #補丁:abs()
        dp = [[0] * (half + 1) for _ in range(len(nums))]

        # base: 第 0 個數
        dp[0][0] = 1
        if nums[0] <= half:
            dp[0][nums[0]] += 1

        for i in range(1, len(nums)):
            for j in range(half + 1):
                # 不選 nums[i]
                dp[i][j] += dp[i-1][j]

                # 選 nums[i]
                if j >= nums[i]:
                    dp[i][j] += dp[i-1][j - nums[i]]
        
        return dp[len(nums)-1][half]