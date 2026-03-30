class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while stones:
            if len(stones) == 1:
                return (-1)*stones[0]
            heavy1st = -heapq.heappop(stones)
            heavy2nd = -heapq.heappop(stones)
            if heavy1st != heavy2nd:
                heapq.heappush(stones, (-1)*abs(heavy1st-heavy2nd))

        return 0    



        


        