/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    let Bignum1 = BigInt(num1)
    let Bignum2 = BigInt(num2)
    return ''+(Bignum1*Bignum2)
};
