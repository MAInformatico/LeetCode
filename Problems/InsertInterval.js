/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {    
    let result = [];
    
    let i = 0;
    while(i < intervals.length && intervals[i][1] < newInterval[0]) {
        result.push(intervals[i]);
        i++;
    }
    
    newInterval = [Math.min(newInterval[0], i < intervals.length ? intervals[i][0] : Infinity), newInterval[1]];    
                                       
    while(i < intervals.length && newInterval[1] >= intervals[i][0]) {
        newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
        i++;
    }       
    result.push(newInterval);
   return result.concat(intervals.slice(i, intervals.length));
    
};
