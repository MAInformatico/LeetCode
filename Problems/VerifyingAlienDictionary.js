/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
    let charChecked = new Map()

    for(let i = 0; i < order.length; i++){
        let char = order[i]
        charChecked.set(char, i)
    }
    for(let j = 1; j < words.length; j++){
        let previous = words[j-1], current = words[j]
        if(charChecked.get(previous[0]) > charChecked.get(current[0]))
            return false
        else if(previous[0] === current[0]){
            let pointer = 1
            while(previous[pointer] === current[pointer])pointer++
            if(current[pointer] === undefined)
                return false
            if(charChecked.get(previous[pointer]) > charChecked.get(current[pointer]))
                return false
        }
    }
    return true
};
