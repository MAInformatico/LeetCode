class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:        
        count=Counter(arr)
        
        if count[0]>1:
            return True
        
        if 0 in count:
            count.pop(0)
        
        for i in count:
            if i*2 in count:
                return True
        
        return False
