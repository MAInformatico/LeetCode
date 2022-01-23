class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        else:
            newS = ''.join(filter(str.isalnum, s)) 
            if newS.lower() == newS[::-1].lower():
                return True
            else:
                return False
