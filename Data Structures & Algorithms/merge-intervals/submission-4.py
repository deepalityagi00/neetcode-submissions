class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_interval = sorted(intervals, key=lambda x: x[0])

        prev_start = sorted_interval[0][0]
        prev_end = sorted_interval[0][1]

        new_intervals = []
        for s, e in sorted_interval:
            if prev_end >= s:
                end = max(prev_end, e)
                interval = [prev_start,end]
                prev_end = end
            else:
                new_intervals.append([prev_start, prev_end])
                prev_start = s
                prev_end=e
        new_intervals.append([prev_start, prev_end])
        return new_intervals
