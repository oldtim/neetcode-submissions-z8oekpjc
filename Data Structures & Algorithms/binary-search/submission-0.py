class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            temp = (left + right)//2
            if nums[temp] == target:
                return temp
            if nums[temp] > target:
                right = temp - 1
            if nums[temp] < target:
                left = temp + 1
        return -1
        
        