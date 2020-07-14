/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    let i, j;
    for (i = nums.length - 2; nums[i] >= nums[i + 1] && i >= 0; i--);
    if (i >= 0) {
        for (j = nums.length - 1; nums[j] <= nums[i]; j--);
            [nums[i], nums[j]] = [nums[j], nums[i]]; //swap
    }
    for (i++, j = nums.length - 1; i < j; i++, j--) {
            [nums[i], nums[j]] = [nums[j], nums[i]];
    }
};
