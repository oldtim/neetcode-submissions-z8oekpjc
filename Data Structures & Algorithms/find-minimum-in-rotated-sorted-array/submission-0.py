class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        while (right - left) > 1:
            mid = (left + right)//2
            if nums[left] > nums[mid]:
                right = mid
            if nums[mid] > nums[right]:
                left = mid
        
        return min(nums[left], nums[right])
            


        