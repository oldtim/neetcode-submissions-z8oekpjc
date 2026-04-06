class Solution:
    def rob(self, nums: List[int]) -> int:
        dfs_dict = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            
            

            if i+2 in dfs_dict:
                plus_2 = dfs_dict[i+2]
            else:
                plus_2 = dfs(i+2)
            if i+1 in dfs_dict:
                plus_1 = dfs_dict[i+1]
            else:
                plus_1 = dfs(i+1)

            ans = max(nums[i] + plus_2, plus_1)
            dfs_dict[i] = ans
            return ans
        
        return dfs(0)



        