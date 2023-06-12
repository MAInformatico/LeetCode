/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    let i = 0, j = 0;
    let result = [];
    while(i < nums.length){
        j = i + 1;
        while(j<nums.length && nums[j]-1===nums[j-1]){
            j++;
        }
        if(i !== j-1){
            result.push(""+nums[i]+"->"+nums[j-1]);
        }
        else{
            result.push(""+nums[i]);
        }
        i = j;
    }
    return result;
};
