/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const addParanthesis = (current, open, close) => {
    if (current.length === n * 2) { //base case
      result.push(current); //we have all the parenthesis
      return;
    }
    if (open < n) { addParanthesis(current + '(', open + 1, close); } //add open parenthesis
    if (close < open) { addParanthesis(current + ')', open, close + 1); } //add close parenthesis
    };
    const result = [];
    addParanthesis('', 0, 0);
    return result;
};
