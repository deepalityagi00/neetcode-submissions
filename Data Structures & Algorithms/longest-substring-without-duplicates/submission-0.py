class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        max_length = 0
        for right in range(len(s)):
            #keep expanding
            window.append(s[right])

            while len(window) != len(set(window)):
                # unstable window
                del window[0]
                        
            #stable window
            max_length = max(max_length, len(window))
        
        return max_length
