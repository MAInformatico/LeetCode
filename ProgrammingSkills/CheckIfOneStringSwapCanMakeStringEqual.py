class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        
        differences = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                differences.append((s1[i], s2[i]))
                       
        return len(differences) == 2 and differences[0][1] == differences[1][0] and differences[0][0] == differences[1][1]
