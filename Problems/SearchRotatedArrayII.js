/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {    
    nums.sort(function(a, b) { return a - b; });
    result = nums.includes(target);
    return result;    
};
