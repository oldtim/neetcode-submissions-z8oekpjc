class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = [0,0,0]
        for i in range(len(triplets)):
            if triplets[i][0] == target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                ans[0] = 1
            if triplets[i][1] == target[1] and triplets[i][0] <= target[0] and triplets[i][2] <= target[2]:
                ans[1] = 1
            if triplets[i][2] == target[2] and triplets[i][1] <= target[1] and triplets[i][0] <= target[0]:
                ans[2] = 1
        if ans[0]*ans[1]*ans[2] == 0:
            return False
        else:
            return True

        