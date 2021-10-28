/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function(s) {
    let current = s.slice(0,10);
    const seen = new Set([current]);
    const result = new Set();
    
    for(let i = 10; i < s.length; i++){
        current = current.slice(1) + s[i];
        if(seen.has(current)) result.add(current);
        seen.add(current);
    }
    return [...result];
};
