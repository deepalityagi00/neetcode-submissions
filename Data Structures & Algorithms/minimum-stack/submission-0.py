from collections import deque
class MinStack:

    def __init__(self):
        self.stack=deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            self.stack.append(val)
            # compare the min_value 
            last_min = self.min_stack[-1]
            if val < last_min:
                self.min_stack.append(val)
            else: 
                self.min_stack.append(last_min)
        

    def pop(self) -> None:
        if not self.stack:
            return None
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.min_stack[-1]
    
