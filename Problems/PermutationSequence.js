/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    const aux = Array.from({length:n}, (_, i) => i+1);
    const currentfact = [1];
    const result = [];
    
    for(let i = 1; i <= aux.length; i++) {
        currentfact.push(currentfact[i-1] * aux[i-1]);
    }
    
    while(aux.length) {
        const idx = Math.ceil(k / currentfact[--n]) - 1;
        result.push(aux.splice(idx, 1));
        k = k % currentfact[n] || currentfact[n]
    }
    return result.join('');
};
