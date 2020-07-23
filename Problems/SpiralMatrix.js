/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    if (!matrix || !matrix.length) return []
    
    let result = [], rows = matrix.length, cols=matrix[0].length
    
    for (let k=0; k<Math.round(Math.min(rows,cols)/2); k++){
		
		// top row
        for (let i=k; i<=cols-k-1; i++) {
            result.push( matrix[k][i] )
        }
		
        for (let j=k+1; j<=rows-k-2; j++) {
            result.push( matrix[j][cols-k-1] )
        }
		
        for (let i=cols-k-1; i>=k; i--) {
            if (rows-k-1 !== k)  result.push( matrix[rows-k-1][i] )
        }
		
        for (let j = rows-k-2; j>=k+1; j--) {
            if (cols-k-1 !== k) result.push( matrix[j][k] )
        }
    }
    return result
};
