class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split(' ')
        dictionary = {}
        if len(set(list(pattern))) != len(set(sList)):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dictionary:
                dictionary[pattern[i]] = sList[i]
        result = []
        for i in pattern:
            result.append(dictionary[i])
        return result == sList
