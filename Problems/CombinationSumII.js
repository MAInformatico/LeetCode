/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    const result = [];
    candidates.sort((a, b) => a - b);
    
    function permutations(arr=[], sum=0, iter=0) { //backtracking algorithm
        if(sum > target) return;
        if(sum === target) result.push(arr);        
        const marked = new Set();
        
        for(let i = iter; i < candidates.length; i++) {
            if(marked.has(candidates[i])) continue;
            permutations([...arr, candidates[i]], sum+candidates[i], i + 1)
            marked.add(candidates[i]);
        }
    }
    permutations()
    return result;
};
