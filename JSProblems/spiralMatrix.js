/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const yLength = matrix.length;
    const xLength = matrix[0].length;
    let y = 0, x = 0, aux = 0;
    let area = xLength * yLength;
    let result = [];

    while(aux < area){
        for(let i = x; aux<area && i<xLength-x; i++){
            result.push(matrix[y][i])
            aux++;
        }
        y++;
        for(let i = y; aux<area && i<yLength-y+1; i++){
            result.push(matrix[i][(xLength - 1) - x])
            aux++;
        }
        x++;

        for(let i = (xLength - 1) - x; aux<area && i>=x-1; i--){
            result.push(matrix[(yLength - 1) - (y - 1)][i])
            aux++;
        }

        for(let i = (yLength - 1) - y; aux<area && i>=y; i--){
            result.push(matrix[i][x - 1])
            aux++;
        }

    }
    return result
};
