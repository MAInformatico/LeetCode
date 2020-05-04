class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def toString(S):
            aux = []
            for i in S:
                if i == '#': #cleaning the string
                    aux and aux.pop()
                else:
                    aux.append(i)
            return ''.join(aux)
        return toString(S) == toString(T)
