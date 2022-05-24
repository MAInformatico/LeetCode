from collections import deque

openParenthesis = '('

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = deque([0])
        push, pop = stack.append, stack.pop
        
        result = 0
        
        for i in s:
            if i  == openParenthesis:
                push(0)
            elif len(stack) > 1:
                paraSize = pop() + 2
                stack[-1] += paraSize
            else:
                result = max(result, stack[0])
                stack[0] = 0
                
        return max(result, max(stack))
