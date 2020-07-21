/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    const result = [];    
    function permute(data, op) { //backtracking algorithm
        if(!op.length) result.push(data);
        
        for(let i = 0; i < options.length; i++) {
            permute([...data, op[i]], [...op.slice(0, i), ...op.slice(i+1)]);
        }
    }
    permute([], nums)
    return result;
};
