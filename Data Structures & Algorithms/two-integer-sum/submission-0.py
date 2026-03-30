class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_diff = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            #if hash_diff[temp]:
            if temp in hash_diff:
                return [hash_diff[temp], i]
            else:
                hash_diff[nums[i]] = i
        
        return []

        