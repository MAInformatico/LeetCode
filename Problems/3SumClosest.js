/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    let sortedArray = nums.sort((a, b) => a - b);
    let numsSize = sortedArray.length;
    let result = null;
    
    for(let i=0; i<=numsSize-2; i++){
        for(let j = i+1; j<numsSize-1;j++){
            for(let k = j+1; k<numsSize; k++){
                let aux = sortedArray[i] + sortedArray[j] + sortedArray[k];
                if(result == null || (Math.abs(result - target) > Math.abs(aux - target)) ) result = aux;                
            }            
        }
    }    
    
    return result;
};
