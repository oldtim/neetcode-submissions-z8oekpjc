class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        ans = [1]*len(nums)
        tmp1 = 1
        tmp2 = 1
        for i in range(1, len(nums)):
            tmp1 = tmp1*nums[i-1]
            prefix[i] = tmp1
        
        for j in range(len(nums)-2, -1, -1):
            tmp2 = tmp2*nums[j+1]
            suffix[j] = tmp2
        
        for k in range(len(nums)):
            ans[k] = prefix[k]*suffix[k]
        
        return ans






        