/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let colors = [0,0,0];
    for(let i = 0; i < nums.length; i++){
        if(nums[i] == 0){
            colors[0]++;
        }
        else if(nums[i] == 1){
            colors[1]++;
        }
        else{
            colors[2]++;
        }
    }
    let index = 0
    for(let j = 0; j < colors[0]; j++){
        nums[index] = 0
        index++
    }
    for(let j = index; j < colors[0] + colors[1]; j++){
        nums[index] = 1
        index++
    }
    for(let j = index; j < colors[0] + colors[1] + colors[2]; j++){
        nums[index] = 2
        index++
    }  
};
