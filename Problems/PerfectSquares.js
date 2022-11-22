/**
 * @param {number} n
 * @return {number}
 */

var dynamicMatrix = new Map();

var numSquares = function(n) {
    let nearestSqrt = Math.sqrt(n);
    if (n === 0){
        return 0;
    }
    if((nearestSqrt%1) === 0){
        return 1;
    }
    if(dynamicMatrix[n] !== undefined){
        return dynamicMatrix[n];
    }
    
    nearestSqrt = Math.floor(nearestSqrt);
    let minimum = n;
    
    for(let i = nearestSqrt; i>1; i--){
        minimum = Math.min(minimum, Math.floor(n/(i*i)) + numSquares(n%(i*i)));
    }
    dynamicMatrix[n] = minimum;
    
    return dynamicMatrix[n];
        
};
