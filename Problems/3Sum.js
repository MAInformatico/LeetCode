/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums = nums.sort(function(a, b){return a-b});
    var result = [];
    for(let i= 0; i< nums.length - 2; i++) {
        if(i== 0 || (i>0 && nums[i] != nums[i-1])) {
           let st = i+1, hi = nums.length -1, sum = 0 - nums[i];
            while(st < hi) {
                if(nums[st]+nums[hi]==sum){ //it is solution
                    result.push([nums[i], nums[st], nums[hi]])
                    while (st < hi && nums[st] == nums[st+1]) {
                        st++;
                    }
                    while (st < hi && nums[hi] == nums[hi-1]) {
                        hi--;
                    }
                    st++;hi--;
                } else if(nums[st]+nums[hi] > sum) {
                      hi--;
                } else {
                    st++;
                }
            }
        }
    }
    return result; 
};
