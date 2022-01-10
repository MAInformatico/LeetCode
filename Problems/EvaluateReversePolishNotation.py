class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
                    "+" : (lambda x,y : x+y),
                    "-" : (lambda x,y : x-y),
                    "*" : (lambda x,y : x*y),
                    "/" : (lambda x,y : x/y)                        
                    }
        stack = []
        
        for i in tokens:
            if i not in operations:
                stack.append(i)
                
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                result = operations[i](int(num2), int(num1))
                stack.append(int(result))
        
        return stack[-1]
