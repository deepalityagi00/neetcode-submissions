from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)

        for idx, word in enumerate(s):
            if freq[word] == 1:
                return idx
        return -1