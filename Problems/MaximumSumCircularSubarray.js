/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubarraySumCircular = function(nums) {
    let currMax = nums[0];
    let currMin = nums[0];
    let sum = currMax;
    let maxSum = currMax;
    let minSum = currMin;
    
    for(let i = 1; i < nums.length; i++){
        currMax = Math.max(nums[i], currMax + nums[i]);
        currMin = Math.min(nums[i], currMin + nums[i]);
        maxSum = Math.max(currMax, maxSum);
        minSum = Math.min(currMin, minSum);
        sum += nums[i];
    }
    
    if(minSum == sum) return maxSum;

    return Math.max(sum - minSum, maxSum);   

};
