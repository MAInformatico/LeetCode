/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    let array = new Array(n + 1).fill(0);

    for(let i of trust){
        array[i[0]] = -1;
        if(array[i[1]] !== -1)
            array[i[1]] += 1;
    }

    for(let i = 1; i<array.length; i++){
        if(array[i] === n - 1)
            return i;
    }
    return -1;
};
