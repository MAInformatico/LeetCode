class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        increase_flag = False
        decrease_flag = False
        current_val = A[0]
        
        for i in A[1:]:
            if i > current_val:        
                if decrease_flag: return False
            if not increase_flag: increase_flag = True
                
            elif i < current_val: 
                if not increase_flag: return False
                if not decrease_flag: decrease_flag = True
                    
            else:
                return False
                current_val = i
        
        return decrease_flag
