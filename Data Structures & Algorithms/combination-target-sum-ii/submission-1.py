##chatGTP建議:

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        temp = []

        def dfs(start, total):
            if total == target:
                ans.append(temp.copy())
                return
            
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                # 🔴 skip duplicates（關鍵）
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                temp.append(candidates[i])
                dfs(i+1, total + candidates[i])  # ⚠️ 不能重複用同一個數
                temp.pop()

        dfs(0, 0)
        return ans