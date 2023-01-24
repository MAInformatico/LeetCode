/**
 * @param {number[][]} board
 * @return {number}
 */
var snakesAndLadders = function(board) {
  const len = board.length;
  const getLoc = (pos) => {
    let row = Math.floor((pos - 1) / len);
    let col = (pos - 1) % len;
    
    col = (row % 2) === 1 ? len - col - 1 : col;
    row = len - row - 1;
    return [row,col];
  }
  
  const q = [1];
  const v = {'1': 0};
  
  while(q.length) {
    const i = q.shift();
    
    if(i === len*len)
        return v[i];
    
    for(let j = i+1; j <= Math.min(i+6, len*len); j++) {
      const [r, c] = getLoc(j);
      const next = board[r][c] === -1 ? j : board[r][c];
      if(v[next] === undefined) {
        q.push(next);
        v[next] = v[i] + 1;
      }      
    }
    
  }
  
  return -1;
};
