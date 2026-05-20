from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        k = len(s1)
        window = Counter()
        left=0
        for right in range(len(s2)):
            window[s2[right]] +=1
            
            if right-left +1 > k:
                char_left = s2[left]
                window[char_left] -=1
                if window[char_left] ==0:
                    del window[char_left]
                left +=1
            if window == need:
                return True
        return False