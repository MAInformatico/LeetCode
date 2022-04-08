class Solution:
    def rob(self, nums: List[int]) -> int:
        memoList = [0,0]
     
        for i in range(len(nums)):
            aux = memoList[0]
            memoList[0] = max(memoList[1] + nums[i], memoList[0])
            memoList[1] = aux
        return memoList[0]
