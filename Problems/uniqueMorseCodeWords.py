class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code = {}
        result = set()
        index =0
        for i in range(97,123):
            code[chr(i)] = morse[index]
            index += 1
        for word in words:
            aux = []
            for i in word:
                aux.append(code[i])
            result.add(''.join(aux))
        return len(result)
