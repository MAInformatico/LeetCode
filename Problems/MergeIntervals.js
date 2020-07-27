/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if(!intervals.length) return [];
    intervals.sort((a, b) => a[0] - b[0]);
    
    const result = [intervals[0]];
    
    for(let [start, end] of intervals) {
        if(start <= result[result.length - 1][1]) {
            const [prevStart,prevEnd] = result.pop();
            result.push([prevStart, Math.max(end, prevEnd)]);
        } else result.push([start, end]);
    }
    return result;
};
