class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def checkIsSubstring(word):
            i = 0
            for j in word:
                try:
                    ind = s.index(j, i)
                    i = ind + 1
                except:
                    return False
            return True

        return sum(checkIsSubstring(it) for it in words)
