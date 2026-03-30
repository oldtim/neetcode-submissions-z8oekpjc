class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack([], nums, [False] * len(nums))
        return self.ans

    def backtrack(self, perm, nums, pick):
        if len(perm) == len(nums):
            self.ans.append(perm.copy())
            return
        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False

            

        