from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)
        heap = []
        for char, freq in freq_map.items():
            heapq.heappush(heap, (-freq, char))
        
        result = ""
        while len(heap) >= 2:
            f1, c1 = heapq.heappop(heap)
            f2, c2 = heapq.heappop(heap)
            result +=c1
            result +=c2
            f1+=1
            f2+=1
            # put the elements back to heap
            if f1 < 0:
                heapq.heappush(heap, (f1, c1))   
            if f2 < 0:
                heapq.heappush(heap, (f2, c2))           
        
        if heap:
            #we have one tuple 
            f,c = heapq.heappop(heap)
            #check if tha last tuple freq
            if result and c == result[-1]:
                return ""
            elif -f > 1:
                return ""
            result +=c
        return result