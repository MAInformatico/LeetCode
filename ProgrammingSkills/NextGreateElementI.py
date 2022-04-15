class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:     
        result = []
        for i in nums1:
            indexNums2 = nums2.index(i)
            for j in nums2[indexNums2+1:len(nums2)]:
                if j > i:
                    result.append(j)
                    break
            else:
                result.append(-1)
        return result
