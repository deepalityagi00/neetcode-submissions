from collections import defaultdict, Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = defaultdict(int)
        s1_seen = Counter(s1)

        def is_permu(seen):
            for char, freq in s1_seen.items():
                seen_freq = seen.get(char, 0)
                if seen_freq < freq:
                    return False
            return True
        
        start = 0
        for end, s_char in enumerate(s2):
            seen[s_char] +=1
            while (end-start+1) > len(s1):
                seen[s2[start]] -=1
                start +=1
            if is_permu(seen):
                return True

        return False 
            