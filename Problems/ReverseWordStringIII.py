class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split()
        result = [aux[::-1] for aux in result]
        result = ' '.join([iterator for iterator in result])
        return result
