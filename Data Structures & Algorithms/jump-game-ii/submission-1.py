class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = nums[0]
        ans = 1  #題目說一定可以到
       
        while right < len(nums)-1:
            next_right = right
            for i in range(left, right+1):     
                next_right = max(next_right, i + nums[i])
            
            ans += 1
            left = right + 1
            right = next_right
        
        return ans

        