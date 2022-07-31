class NumArray:
    nums = []
    aux = 0
    length = 0
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.aux = sum(nums)
        self.length = len(nums)

    def update(self, index: int, val: int) -> None:
        self.aux -= self.nums[index]
        self.nums[index] = val
        self.aux += self.nums[index]

    def sumRange(self, left: int, right: int) -> int:
        if right - left > self.length // 2:
            result = sum(self.nums[:left]) + sum(self.nums[right + 1:])
            return self.aux - result
        else:
            return sum(self.nums[left: right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
