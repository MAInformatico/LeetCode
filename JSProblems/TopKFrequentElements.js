/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let frequencies = new Map();
    for (let i = 0; i < nums.length; i++) {
        if (frequencies.has(nums[i])) {
            frequencies.set(nums[i], frequencies.get(nums[i]) + 1)
        } else {
            frequencies.set(nums[i], 1)
        }
    }
    
    let result = [...frequencies.keys()].sort((a, b) => frequencies.get(b) - frequencies.get(a)).slice(0, k)
    
    return result;
};
