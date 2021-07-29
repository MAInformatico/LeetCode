class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtracking(text: str):
            if not text:
                result.append(current[:])
            for end in range(1, len(text) + 1):
                if text[:end] == text[end-1::-1]:
                    current.append(text[:end])
                    backtracking(text[end:])
                    current.pop()
        result = []
        current = []
        backtracking(s)
        return result        
