class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table={}
        for i in range(len(nums)):
            hash_table[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in hash_table:
                if hash_table[target-nums[i]] != i:
                    return [i, hash_table[target-nums[i]]]
        return []
