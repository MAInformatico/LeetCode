class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(self.expandAndCountPallindromes(i,i,s) + self.expandAndCountPallindromes(i,i+1,s) for i in range(len(s)))
    
    def expandAndCountPallindromes(self, i, j, s):        
        length=len(s)
        count=0
        
        while 0<=i and j<length and s[i]==s[j]:
            i-=1
            j+=1
            count+=1
        
        return count
