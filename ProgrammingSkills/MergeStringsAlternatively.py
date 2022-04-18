class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:        
        difference = ""
        if len(word1) > len(word2):
            difference = word1[len(word2):]
        elif len(word1) < len(word2):
            difference = word2[len(word1):]            
        else:
            difference = ""
        
        result =""
        for iterator1,iterator2 in zip(word1, word2):
            result += iterator1 + iterator2
            
        return result + difference
