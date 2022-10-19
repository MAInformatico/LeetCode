class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = Counter(words)
        result = sorted(frequencies, key = lambda x: (-frequencies[x],x))
        return result[:k]
