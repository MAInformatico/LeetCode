class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [s]
        for iterator, characterChecker in enumerate(s):
            if characterChecker.isalpha():
                resultLen = len(result)
                for j in range(resultLen):
                    newPermutation = list(result[j])
                    newPermutation[iterator] = newPermutation[iterator].swapcase()
                    result.append(''.join(newPermutation))
                                
        return result
