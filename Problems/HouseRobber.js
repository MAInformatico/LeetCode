/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (!nums.length)
        return 0;
    if (nums.length === 1)
        return nums[0];
    if (nums.length === 2)
        return Math.max(nums[0], nums[1]);
    
    let maxTwoBefore = nums[0];
    let maxOneBefore = Math.max(nums[0], nums[1]);
    
    for (let i = 2; i < nums.length; i++) {
        const maxCurrent = Math.max(nums[i] + maxTwoBefore, maxOneBefore);
        
        maxTwoBefore = maxOneBefore;
        maxOneBefore = maxCurrent;
    }
    
    return maxOneBefore;

};
