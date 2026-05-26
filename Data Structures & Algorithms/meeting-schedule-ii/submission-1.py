"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = 1
        if len(intervals) <= 1:
            return len(intervals)
        intervals.sort(key=lambda x: x.start)
        base_list = [intervals[0].end]
        for i in range(1, len(intervals)):
            if base_list[0] <= intervals[i].start:
                heapq.heappop(base_list)
                heapq.heappush(base_list, intervals[i].end)
            else:
                rooms += 1
                heapq.heappush(base_list, intervals[i].end)
        return rooms

        

        