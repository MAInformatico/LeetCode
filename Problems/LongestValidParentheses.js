/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    let stack = [] , aux = Array(s.length+1).fill(0), result=0;
    for(let i=0; i<s.length;i++){
        if(s.charAt(i) == '(') stack.push(i);
        else{
            if(stack.length != 0){
                let lastValue = stack.pop()
                aux[i+1] += (2 + aux[i] + aux[lastValue])
                result = Math.max(result,aux[i+1])
            }
        }        
    }
    return result;
};
