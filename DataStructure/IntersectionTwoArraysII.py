class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary = {}
        result = []
        
        for i in nums1:
            if i in dictionary:
                dictionary[i] = dictionary[i] + 1
            else:
                dictionary[i] = 1
        
        for i in nums2:
            if i in dictionary and result.count(i) != dictionary[i]:
                result.append(i)
        
        return result
