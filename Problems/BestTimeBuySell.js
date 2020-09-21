/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let result = 0, curr = prices[0];
    
    for(let x of prices) {
        if(curr < x) result = Math.max(result, x - curr);
        else curr = x;
    }
    return result;
};
