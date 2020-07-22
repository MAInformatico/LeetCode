/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    const size = height.length;
    const lSideMax = new Array(size);
    const rSideMax = new Array(size);
    let result = 0
    
    lSideMax[0] = height[0]
    rSideMax[size - 1] = height[size - 1];
    
    for (let i = 1; i < size; i++) {
        lSideMax[i] = Math.max(height[i], lSideMax[i - 1]);
    }
    
    for (let i = size - 2; i >= 0; i--) {
        rSideMax[i] = Math.max(height[i], rSideMax[i + 1]);
    }

    for (let i = 1; i < size - 1; i++) {
        result += Math.min(lSideMax[i], rSideMax[i]) - height[i]   
    }    
    return result;
    
};
