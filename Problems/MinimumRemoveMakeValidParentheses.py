class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  
        listS = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    listS[i] = ''
        for it in stack:
            listS[it] = ''
        
        return "".join(listS)
