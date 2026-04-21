class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i_1st in range(len(nums)):
            # if nums[i_1st] > 0:    #解省runtime
            #     break

            if i_1st > 0 and nums[i_1st] == nums[i_1st-1]:
                continue

            i_2nd, i_3rd = i_1st + 1, len(nums) - 1
            while i_2nd < i_3rd:
                threeSum = nums[i_1st] + nums[i_2nd] + nums[i_3rd]
                if threeSum > 0:
                    i_3rd -= 1
                elif threeSum < 0:
                    i_2nd += 1
                else:
                    ans.append([nums[i_1st], nums[i_2nd], nums[i_3rd]])
                    i_2nd += 1
                    i_3rd -= 1
                    while nums[i_2nd] == nums[i_2nd-1] and i_2nd < i_3rd:
                        i_2nd += 1

        return ans

# 直接看解答      