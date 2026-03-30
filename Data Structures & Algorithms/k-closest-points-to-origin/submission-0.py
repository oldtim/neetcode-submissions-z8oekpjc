class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for p in points:
            tmp_d = math.sqrt(p[0]*p[0] + p[1]*p[1])
            distance.append((tmp_d, p))
        heapq.heapify(distance)
        ans = []
        for _ in range(k):
            ans.append(distance[0][1])
            heapq.heappop(distance)
        return ans
        