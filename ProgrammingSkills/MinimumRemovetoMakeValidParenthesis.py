class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        countOpen = 0
        countClosed = sum(1 for x in s if x == ')')
        result = []
        for c in s:
            if c == '(':
                if countClosed > countOpen:
                    countOpen += 1
                else:
                    continue
            if c == ')':
                countClosed -= 1
                if countOpen > 0:
                    countOpen -= 1
                else:
                    continue
            result.append(c)
        return ''.join(result)
