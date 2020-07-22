/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    const result = [];       
    function permute(ops, arr=[]) {
        if(!ops.length) result.push(arr);
        const exits = new Set();
        
        for(let i = 0; i < ops.length; i++) {
            if(exits.has(ops[i])) continue;
            permute([...ops.slice(0, i), ...ops.slice(i+1)], [...arr, ops[i]]);
            exits.add(ops[i]);
        }
    }
    permute(nums);
    return result;    
};
