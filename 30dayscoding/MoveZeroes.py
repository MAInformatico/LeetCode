class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        counter = 0
        for i in range(len(nums)):
            if (nums[i])!=0 :
                nums[counter] = nums[i];
                counter += 1;
        
        while(counter < len(nums)):
            nums[counter] = 0;
            counter += 1;
