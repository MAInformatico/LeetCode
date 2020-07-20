/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

var combinationSum = function(candidates, target) {
    const result = [];
    
    function permutations(arr=[], sum=0, iter=0) { //backtracking algorithm
        if(sum > target) return;
        if(sum === target) result.push(arr);
        
        for(let i = iter; i < candidates.length; i++) {
            permutations([...arr, candidates[i]], sum+candidates[i], i);
        }
    }
    permutations()
    return result;
};
