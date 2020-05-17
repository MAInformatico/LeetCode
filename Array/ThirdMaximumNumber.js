/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    let aux = Array.from(new Set(nums));
    if (aux.length < 3) return Math.max(...aux);
    aux.splice(aux.indexOf(Math.max(...aux)), 1);
    aux.splice(aux.indexOf(Math.max(...aux)), 1);
    return Math.max(...aux);
};
