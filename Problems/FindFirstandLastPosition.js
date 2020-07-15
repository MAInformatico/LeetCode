/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    let i = 0;
    while(i < nums.length) {
        let current = nums[i];
        let j = i;
        if(current == target) {
            while(j < nums.length && nums[j] === target) {
                j++;    
            }
            return [i, --j]
        }
        i++;
    }
    return [-1, -1];
};
