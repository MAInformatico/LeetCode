/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    for(let i=1; i<Number.MAX_SAFE_INTEGER; i++){
        if(nums.includes(i)){
            continue;
        }else{
            return i;
        }
    }
};
