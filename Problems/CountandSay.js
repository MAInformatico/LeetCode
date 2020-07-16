/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    if (n == "1") return n.toString();
  
    return countAndSay(n-1)
        .match(/1+|2+|3+|4+/g)
        .reduce((acc, nums) => acc += `${nums.length}${nums[0]}`, '')
};
