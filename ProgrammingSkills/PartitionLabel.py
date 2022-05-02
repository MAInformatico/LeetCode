class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dictionary={}
        for i,c in enumerate(s): 
            dictionary[c] = i
        
        result = []
        begin, end = 0, 0
        for i,c in enumerate(s):
            end = max(end, dictionary[c])
            if end == i:
                result.append(end+1 - begin)
                begin = i+1
        
        return result
