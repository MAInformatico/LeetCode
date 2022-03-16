class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        auxStack = deque([])
        popIndex = 0
        
        for it in pushed:
            auxStack.append(it)
            
            while auxStack and auxStack[-1] == popped[popIndex]:
                auxStack.pop()
                popIndex += 1
        
        return not auxStack
