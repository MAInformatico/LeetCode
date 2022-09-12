class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        numTokens = len(tokens)
        i, j = 0, numTokens
        score, result = 0, 0        
        tokens.sort()
        
        while i < j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
                result = max(result, score)
            elif score >= 1 and j > i + 1:
                j -= 1
                power += tokens[j]
                score -= 1
            else:
                return result
        
        return result
