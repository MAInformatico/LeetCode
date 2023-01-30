/**
 * @param {number} n
 * @return {number}
 */

var baseCase = [0,1,1];

var tribonacci = function(n) {
    if(baseCase[n] !== undefined)
        return baseCase[n];
    
    if(n>=0)
        baseCase[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3);

    return baseCase[n];
};
