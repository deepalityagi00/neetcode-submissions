from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        size = n+1
        total_time = 0
        freq_tasks = Counter(tasks)
        max_freq = []
        for item, freq in freq_tasks.items():
            heapq.heappush(max_freq, (-freq, item))
        
        while max_freq:
            hold_ele = []
            ran = 0
            for i in range(size):
                if max_freq:
                    freq, item = heapq.heappop(max_freq)
                    freq = -(freq + 1)
                    if freq > 0:
                        hold_ele.append((-freq, item))
                    ran +=1
                else:
                    break
            
            for ele in hold_ele:
                heapq.heappush(max_freq, ele)
            
            if max_freq:
                total_time +=size
            else:
                total_time +=ran

        return total_time 


