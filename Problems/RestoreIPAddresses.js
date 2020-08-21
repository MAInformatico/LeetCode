/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    let IP = [];    
    function permute(oct, str) {
        if(oct.length === 3) {
            if(isValid(str)) IP.push([...oct, str]);
            return;
        }
        
        for(let i = 1; i < 4; i++) {
            let subStr = str.slice(0, i);
            if(!isValid(subStr)) continue;
            permute([...oct, subStr], str.slice(i));
        }
    }
    
    function isValid(str) {
        if(+str > 255 || !str.length) return false;
        if(str.length >= 2 && str[0] === '0') return false;
        return true;
    }
    
    permute([], s);
    return IP.map(x => x.join('.'))
    
};
