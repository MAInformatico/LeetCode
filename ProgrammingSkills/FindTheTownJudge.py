class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if n==1 and trust==[]:
            return 1
        
        s = set()
        for i in trust:
            if i[0] not in s:
                s.add(i[0])        
                
        dictionary = {}
        for i in range(1,n+1):
            if i not in s:
                dictionary[i] = 0
        
        for i in trust:
            if i[1] in dictionary:
                dictionary[i[1]]+=1
                if dictionary[i[1]] == n-1:
                    return i[1]
                  
        return -1
