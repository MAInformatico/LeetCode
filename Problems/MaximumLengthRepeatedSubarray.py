class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        matrix = [[0] * (m + 1) for _ in range (n+1)]
        
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    matrix[i+1][j+1] = matrix[i][j] + 1                    
        
        return max(map(max, matrix))
