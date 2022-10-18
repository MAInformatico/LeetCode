class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"        
        recursiveCall = self.countAndSay(n-1)
        result = ""
        initial = recursiveCall[0]
        iterator = 1
        for i in range(1,len(recursiveCall)):
            if recursiveCall[i] == initial:
                iterator += 1
            else:
                result += str(iterator)
                result += str(initial)
                initial = recursiveCall[i]
                iterator = 1
        result += str(iterator)
        result += str(initial)
        return result
