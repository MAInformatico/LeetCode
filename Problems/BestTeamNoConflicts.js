/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function(scores, ages) {
    let n = scores.length;
    let points = scores.map((x, i) => [x, ages[i]]);
    
    points.sort((a, b) => { 
        if (a[1] != b[1])
            return a[1] - b[1];
        return a[0] - b[0];
    });
    let dynamicMatrix = Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (points[j][0] <= points[i][0])
                dynamicMatrix[i] = Math.max(dynamicMatrix[i], dynamicMatrix[j]);
        }
        dynamicMatrix[i] += points[i][0];
    }
    return Math.max(...dynamicMatrix);  
};
