/**
 * @param {character[][]} maze
 * @param {number[]} entrance
 * @return {number}
 */
var nearestExit = function(maze, entrance) {
    const visited = new Array(maze.length).fill(undefined);
    
    for(const row in visited){
        visited[row] = new Array(maze[row].length).fill(false);
    }
    
    let [steps, remaining, finish] = [0, 1, false];
    const queue = [entrance];
    visited[entrance[0]][entrance[1]] = true;
       
    while(queue.length > 0){
        if (remaining === 0){
            steps++;
            remaining = queue.length;
        }
        
        const cell = queue.shift();
        const [row, column] = cell;
        remaining--;
        
        
        if((row === 0 || row === maze.length - 1 || column === 0 || column === maze[row].length - 1) && (row !== entrance[0] || column !== entrance[1])){
            finish = true;
            break;
        } 

        //top
        if((row-1) > -1 && maze[row-1][column] === '.' && !visited[row - 1][column]){
            queue.push([row-1, column]);
            visited[row-1][column] = true;
        }
        //down
        if((row+1) < maze.length && maze[row+1][column] === '.' && !visited[row + 1][column]){
            queue.push([row+1, column]);
            visited[row+1][column] = true;
        }
        //left
        if(maze[row][column - 1] === '.' && !visited[row][column-1] ){
            queue.push([row, column-1]);
            visited[row][column-1] = true;
        }
        //right
        if(maze[row][column + 1] === '.' && !visited[row][column+1] ){
            queue.push([row, column+1]);
            visited[row][column+1] = true;
        }        
    }
    
    return(steps && finish) ? steps : -1;
    
};
