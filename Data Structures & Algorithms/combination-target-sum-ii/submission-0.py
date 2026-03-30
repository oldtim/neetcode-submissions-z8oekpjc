class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        temp = []
        
        def dfs(i, total):
            if total == target:
                ans.append(temp.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            temp.append(candidates[i])
            total_plus = total + candidates[i]
            dfs(i+1, total_plus)
            temp.pop()

            while i+1 < len(candidates):
                if candidates[i] == candidates[i+1]:
                    i = i + 1               
                else:
                    break
            
            dfs(i+1, total)

            ##第一次寫順序錯誤，           
            # temp.append(candidates[i])
            # total_plus = total + candidates[i]
            # while i+1 < len(candidates):
            #     if candidates[i] == candidates[i+1]:
            #         i = i + 1               
            #     else:
            #         break
            # dfs(i+1, total_plus)
            # temp.pop()
            # dfs(i+1, total)
        
        dfs(0, 0)
        return ans
            

            
            
                


        