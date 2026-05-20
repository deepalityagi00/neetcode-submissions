from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left=0
        window = Counter()
        min_len = float("inf")
        for right in range(len(s)):
            window[s[right]] +=1

            while not need - window:
                # keep shrinking to find the min
                if  right-left+1 < min_len:
                    start_index = left
                    min_len = right-left+1

                window[s[left]] -=1
                if window[s[left]] == 0:
                    del window[s[left]]
                left +=1
        if min_len == float("inf"):
            return ""
        else :
            return s[start_index:start_index+min_len]
            
