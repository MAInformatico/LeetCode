class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        result = 0
        for i in data:
            if result:
                if i > 191 or i < 128:
                    return False
                result -= 1            
            else:
                if i > 247:
                    return False
                if i > 239:
                    result = 3
                elif i > 223:
                    result = 2
                elif i > 191:
                    result = 1
                elif i > 127 or i < 0:
                    return False
        return not result
