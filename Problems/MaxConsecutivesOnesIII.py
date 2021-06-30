class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:        
        previousPos,i,countZeros = 0,0,0 
        for i in range(len(nums)):
            if nums[i] == 0:
                countZeros += 1
            if countZeros > k:
                if nums[previousPos] == 0:
                    countZeros -= 1
                previousPos += 1
        return i-previousPos+1   
