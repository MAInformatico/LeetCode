class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right, mid = 0, num, 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if (mid * mid == num):
                return True
            elif (mid * mid < num):
                left = mid + 1
            else:
                right = mid - 1
        
        return False
