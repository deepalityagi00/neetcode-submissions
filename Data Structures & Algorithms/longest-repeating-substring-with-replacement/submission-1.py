from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window= defaultdict(int)
        start = 0
        max_length = 0
        max_frequency = 0
        for end, char in enumerate(s):
            window[char]+=1
            max_frequency = max(max_frequency, window[char])

            while (end-start+1) - max_frequency > k:
                window[s[start]] -=1
                start +=1
            
            max_length = max(max_length, end-start+1)
        return max_length

