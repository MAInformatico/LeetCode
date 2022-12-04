/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumAverageDifference = function(nums) {
    const len = nums.length
    let leftSum = 0, min = Infinity, result = 0;
    let rightSum = nums.reduce((acc, val) => acc + val);
    
    for (let i = 0; i < len; i++) {
        leftSum += nums[i]
        rightSum -= nums[i]
        
        const leftAverage = Math.floor(leftSum / (i + 1))
        const rightAverage = Math.floor(rightSum / (len - i - 1) || 0) 
        
        const difference = Math.abs(leftAverage - rightAverage)
        if (difference < min) {
            min = difference
            result = i
        }
    }
    
    return result
    
};
