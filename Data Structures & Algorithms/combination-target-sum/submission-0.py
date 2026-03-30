class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        temp = []
        total_sum = 0

        def branch(i, total):
            if total == target:
                ans.append(temp.copy())
                return
    
            if total > target or i == len(nums):
                return
            
            # 選 nums[i]（可以重複）
            temp.append(nums[i])
            branch(i, total + nums[i])
            temp.pop()
            
            # 不選 nums[i]
            branch(i + 1, total)

        branch(0, 0)
        return ans



        ##寫法錯誤，我是想在末端將sum歸位=0，但其實下一截點不是從sum=0開始
        # def branch(i):
        #     nonlocal total_sum

        #     if total_sum == target:
        #         ans.append(temp.copy())
        #         total_sum = 0
                
        #     elif total_sum > target:
        #         total_sum = 0
                
        #         return
        #     else:
        #         temp.append(nums[i])
        #         total_sum = total_sum + nums[i]
        #         branch(i)
        #         if len(nums) > (i+1):
        #             branch(i+1)
        #         else: 
        #             return
        #         temp.pop()
        #         if len(nums) > (i+1):
        #             branch(i+1)
        #         else: 
        #             return
        
        # branch(0)
        # return ans

                
                

                

        