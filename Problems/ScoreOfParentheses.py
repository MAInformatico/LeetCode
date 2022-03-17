class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        result = 0
        
        for i in s:
            
            if i == '(':
                stack.append(result)
                result = 0
                
            else:
                result += stack.pop() + max(result,1)
                
        
        return result    
