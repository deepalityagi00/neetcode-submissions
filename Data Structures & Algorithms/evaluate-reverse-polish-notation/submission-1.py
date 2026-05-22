from collections import deque
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque(tokens)
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        def get_stack(stack):
            if len(stack) > 0:
                element = stack.pop()
                if element in ('+', '-', '*', '/'):
                    right = get_stack(stack)
                    left = get_stack(stack)
                    return int(ops[element](left, right))
                else:
                    return int(element)
            return None

        while stack:
            token = stack.pop()
            if token in ('+', '-', '*', '/'):
                right = get_stack(stack)
                left = get_stack(stack)
                return int(ops[token](left, right))
            else:
                return int(token)
        return None

