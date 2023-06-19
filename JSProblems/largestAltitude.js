/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
  let result = 0;
  let current = 0;
  for (let i = 0; i < gain.length; i++){
      current += gain[i];
      if (current >= result){
          result = current;
      }
  }  
    return result;
};
