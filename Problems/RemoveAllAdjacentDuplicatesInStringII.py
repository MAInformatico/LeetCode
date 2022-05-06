class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack, current = [], ""
        
        for i in s:
            if current and i != current[-1]:
                stack.append(current)
                current = ""
            current += i
            
            while len(current) >= k:
                if not stack:
                    current = ""
                    break
                current = stack.pop()
        
        stack.append(current)
        return "".join(stack)
