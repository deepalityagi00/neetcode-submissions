class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        word = "".join(c.lower() for c in s if c.isalnum())
        end=len(word) -1
        while start < end:
            first = word[start]
            last = word[end]
            if first != last:
                return False
            start +=1
            end -=1
        return True

