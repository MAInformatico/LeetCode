/**
 * @param {number[]} changed
 * @return {number[]}
 */
var findOriginalArray = function(changed) {
    changed.sort((a,b) => a - b);
    
    const dictionary = {};
    for(const i of changed){
        dictionary[i] = ++dictionary[i] || 1;        
    }
    
    const result = [];
    
    for(const i of changed){
        if(dictionary[i]){
            dictionary[i] = --dictionary[i];
            if (dictionary[i * 2]){
                dictionary[i * 2] = --dictionary[i * 2];
                result.push(i);
            }
            else{
                return [];
            }
        }
    }
    
    return result.length * 2 === changed.length ? result : [];
};
