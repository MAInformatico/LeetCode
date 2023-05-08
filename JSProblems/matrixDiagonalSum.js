/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let result = 0;
    let lastPos = mat[0].length;
    let mid = Math.floor( lastPos / 2 );

    for(let i  = 0; i<lastPos; i++){
        result += mat[i][i];
        result += mat[lastPos-1-i][i];            
    }
    if( lastPos % 2 == 1 ){        
        result -= mat[mid][mid];
    }
    return result;  
};
