/**
 * @param {string} s
 * @return {number}
 */
var minFlipsMonoIncr = function(s) {
    let numZeros = 0;

    for(const value of s){
        if (value === "0")
            numZeros += 1;
    }

    let result = numZeros;
    for(let i = 0; i < s.length; i++){
        if(s[i] === "0"){
            numZeros -= 1;
            result = Math.min(result,numZeros);
        }
        else{
            numZeros += 1;
        }
    }
    return result;
};
