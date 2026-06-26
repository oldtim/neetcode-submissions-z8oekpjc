class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = 0
        count_0 = 0
        for n in nums:
            total += n
            if n == 0:
                count_0 += 1

        if total < abs(target) or ((total-abs(target))%2) != 0:  #abs()
            return 0
        if total == abs(target):
            return pow(2, count_0)

        half_target = (total-abs(target))//2    #abs()
        dp2 = [[0]*(half_target + 1) for _ in range(len(nums))]
        if nums[0] <= half_target:
            dp2[0][nums[0]] = 1 
        for i in range(1, len(nums)):
            if nums[i] <= half_target:
                dp2[i][nums[i]] = 1 
            for j in range(half_target+1):  # +1
                dp2[i][j] += dp2[i-1][j] 
                if dp2[i-1][j] != 0 and (j+nums[i]) <= half_target:
                    dp2[i][j+nums[i]] += dp2[i-1][j]
        
        return dp2[len(nums)-1][half_target]



        