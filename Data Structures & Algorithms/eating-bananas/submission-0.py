class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left+right) // 2
            total_t = 0
            for i in range(len(piles)):
                tmp_t = (piles[i] + mid - 1) // mid
                total_t = total_t + tmp_t
            if total_t <= h:
                right = mid
            else:
                left = mid + 1
        return left

            
        