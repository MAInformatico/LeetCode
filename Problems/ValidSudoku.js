/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    for(let i = 0; i < 9; i++){
        let row = new Set();
        let column = new Set();
        let box = new Set();
        
        for(let j = 0; j < 9; j++){         
            let localRow = board[i][j];
            let localColumn = board[j][i];
            let localBox = board[3*Math.floor(i/3)+Math.floor(j/3)][3*(i%3)+(j%3)];
            if(localRow != '.'){
                if(row.has(localRow)) return false;
                row.add(localRow);
            }
            if(localColumn != '.'){
                if(column.has(localColumn)) return false;
                column.add(localColumn);
            }            
            if(localBox != '.'){
                if(box.has(localBox)) return false;
                box.add(localBox);
            }            
        }
    }
    return true;
};
