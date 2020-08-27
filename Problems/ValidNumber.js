/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    const number = s.trim();
    return /^[+-]?([0-9]+|[0-9]+\.[0-9]*|[0-9]*\.[0-9]+)(e[+-]?[0-9]+)?$/.test(number);    
};
