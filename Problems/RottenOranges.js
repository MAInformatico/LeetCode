/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    let auxQueue = []
    let fresh = 0
    let adjacents = [[1,0], [-1,0], [0,1], [0,-1]]
    let result = 0

    for(let i=0; i<grid.length; i++) {
        for(let j=0; j<grid[0].length; j++) {0
            if(grid[i][j] === 1) {
                fresh++
            } else if(grid[i][j] === 2) {
                auxQueue.push([i, j])
            }
         }
    }

    while(auxQueue.length > 0 && fresh > 0) {
        let len = auxQueue.length
    
        while(len) {
            let [x,y] = auxQueue.shift()
        
            for(let [dx, dy] of adjacents) {
                let nextX = x + dx
                let nextY = y + dy
            
               if(nextX < 0 || nextX >= grid.length || nextY < 0 || nextY >= grid[0].length || grid[nextX][nextY] !== 1) continue
            
                fresh--
                grid[nextX][nextY] = 2
                auxQueue.push([nextX, nextY])
            }
            len--
        }
        result++
    }
    return fresh ? -1 : result
};
