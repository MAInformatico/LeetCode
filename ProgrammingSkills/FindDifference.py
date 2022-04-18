class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dictionary = collections.Counter(s)
        for i in t:
            if i not in dictionary or dictionary[i] != t.count(i):
                return i
        return None
