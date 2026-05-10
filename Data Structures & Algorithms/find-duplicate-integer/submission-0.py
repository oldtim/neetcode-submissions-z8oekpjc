class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] < 0:
                return temp+1
            else:
                nums[temp] *= -1




# 一開始也是想到額外開hash來找到重複，但如此空間複雜度O(N)
# 看hint之後寫，發現此題是一種優化空間的模板


        