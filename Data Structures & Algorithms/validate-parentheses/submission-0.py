from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stacks = {"}": "{", "]": "[",")":"("}
        stack = deque()
        for bracket in s:
            if bracket in ['(', '{','[']:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                poped = stack.pop()
                if stacks[bracket] != poped:
                    return False
        
        return len(stack) == 0