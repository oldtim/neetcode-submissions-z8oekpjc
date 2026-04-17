class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        heapq.heapify(intervals)
        base_case = heapq.heappop(intervals)
        origin_len = len(intervals)
        for i in range(origin_len):
            compare_case = heapq.heappop(intervals)
            if base_case[1] < compare_case[0]:
                ans.append(base_case)
                base_case = compare_case
            else:
                base_case[1] = max(base_case[1], compare_case[1])
        
        ans.append(base_case)
        return ans


        