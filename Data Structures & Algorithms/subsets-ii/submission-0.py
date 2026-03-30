class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        nums.sort()
        def dfs(i):
            if i >= len(nums):
                ans.append(temp.copy())
                return

            temp.append(nums[i])
            dfs(i+1)
            temp.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i = i + 1
            dfs(i+1)
        dfs(0)
        return ans

            

        