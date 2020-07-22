/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const result = [];    
    function permute(data, ops) { //backtracking algorithm
        if(!ops.length) result.push(data);
        
        for(let i = 0; i < ops.length; i++) {
            permute([...data, ops[i]], [...ops.slice(0, i), ...ops.slice(i+1)]);
        }
    }
    permute([], nums)
    return result;
};
