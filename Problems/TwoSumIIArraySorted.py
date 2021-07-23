/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let i = 0;
    let j = numbers.length - 1;
    let result = []

    while(i < j){
        let aux = numbers[i] + numbers[j];
        if(aux > target){
            j--;
        }else if(aux < target){
            i++;
        }else{
            result.push(i+1);
            result.push(j+1);
            return result;
        }
    }            
};
