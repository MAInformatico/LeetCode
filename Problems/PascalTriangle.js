/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    const result = [];
    if (numRows > 0) result.push([1]);
    
    if (numRows > 1) result.push([1, 1]);
    
    for (let i = 2; i < numRows; i++) {
        result.push(result[i-1].concat(0).map((v, idx, ori) => v + ori[ori.length - idx - 1])
        );
    }
    return result;
};
