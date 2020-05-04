class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1 = collections.Counter(nums1)
        for i in nums2:
            if i in nums1:
                result.append(x)
                nums1[i] -= 1
                if nums1[i] == 0:
                    del nums1[i]
        return result
