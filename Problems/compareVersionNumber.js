/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    version1 = version1.split('.');
    version2 = version2.split('.');
    
    let i = 0;    
    while (i < version1.length || i < version2.length) {
        const num1 = version1[i] ? parseInt(version1[i]) : 0;
        const num2 = version2[i] ? parseInt(version2[i]) : 0;
        
        if (num1 < num2)  return -1;
        
        else if (num1 > num2) return 1;
        
        else  i+=1;
        
    }
    
    return 0;
};
