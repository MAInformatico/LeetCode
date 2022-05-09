class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) is 0:
            return ""
        
        dictionary = {"2":["a","b","c"],
                      "3":["d","e","f"],
                      "4":["g","h","i"],
                      "5":["j","k","l"],
                      "6":["m","n","o"],
                      "7":["p","q","r","s"],
                      "8":["t","u","v"],
                      "9":["w","x","y","z"]}
            
        aux = list(dictionary[digits[0]])
        if len(digits) is  1:
            return aux
            
        result = []
        index = self.letterCombinations(digits[1:])
        for i in aux:
            for j in index:
                result.append(i + j)
                    
        return result
