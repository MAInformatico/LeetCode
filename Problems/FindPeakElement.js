/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        const middle = ((left + right) / 2) | 0;
        if (nums[middle] > nums[middle + 1]) {
            right = middle;
        }
        else {
            left = middle + 1;
        }
    }
    return right;
};
