class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
    
        def branch(i):
            if i >= len(nums):
                ans.append(tmp.copy())
                return
            tmp.append(nums[i])
            branch(i+1)
            tmp.pop()
            branch(i+1)
        
        branch(0)
        return ans



#我直接看答案，但我一開始的想法就是用function內有兩個function來遞迴，只是卡在思維定式:
#->我之前做的題目都是要靠function回傳值來給答案，結果這題跟我說可一面遍歷function一面給答案
#也就是我之前以為function只有在遍歷完成後回溯才能給答案

        
        





        