class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count, numbers = 0, Counter(nums)
        for i in range(max(nums), -1, -1):
            count += numbers[i]
            if count == i: 
                return count
        return -1
