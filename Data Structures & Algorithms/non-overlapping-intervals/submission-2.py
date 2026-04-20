class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        heapq.heapify(intervals)
        case1 = heapq.heappop(intervals)
        prevEnd = case1[1]
        ans = 0
        while intervals:
            case2 = heapq.heappop(intervals)
            if case1[1] <= case2[0]:
                prevEnd = case2[1]
                case1 = case2
            elif case1[1] > case2[1]:
                ans += 1
                prevEnd = case2[1]
                case1 = case2
            else:
                ans += 1
                prevEnd = case1[1]
        
        return ans

                

        