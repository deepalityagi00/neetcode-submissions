"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort by start time 
        heap = sorted(intervals, key=lambda x: x.start)
        rooms = []
        for interval in heap:
            # pick the smallest start time
            if rooms:
                latest_end = rooms[0]
                if interval.start >= latest_end:
                    heapq.heappushpop(rooms,interval.end)
                else:
                    heapq.heappush(rooms, interval.end)
            else:
                heapq.heappush(rooms, interval.end)
        return len(rooms)