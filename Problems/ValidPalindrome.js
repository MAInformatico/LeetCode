/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    var re = /[\W_]/g;
    var lowercaseStr = s.toLowerCase().replace(re, '');
    var reverseStr = lowercaseStr.split('').reverse().join(''); 
    return reverseStr === lowercaseStr;
};
