class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start= 0
        end = 0
        max_len = 0
        for idx, char in enumerate(s):
            while start<=idx and char in s[start:idx]:
                start +=1
            end = idx
            max_len = max(max_len, end-start+1)
        return max_len