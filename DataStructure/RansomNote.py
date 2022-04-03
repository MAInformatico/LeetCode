class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteChars = Counter(ransomNote)
        magazineChars = Counter(magazine)
        
        for i in noteChars:
            if(noteChars[i] > magazineChars[i]):
                return False
        return True
