/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    let freqs = new Map();
    for (let i = 0; i < s.length; i++) {
        freqs.set(s[i], freqs.get(s[i]) + 1 || 1);
    }
    let arr = Array.from(freqs.entries());
    arr.sort((a,b) => b[1] - a[1]);
    let result = [];
    for (let i = 0; i < arr.length; i++) {
      for(let j = 0; j< arr[i][1]; j++){
          result.push(arr[i][0]);
      }
    }
     
    return result.join("");  
};
