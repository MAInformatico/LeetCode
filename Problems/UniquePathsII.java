class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if(obstacleGrid == null || obstacleGrid.length == 0) 
			return 0;
        for(int i = 0 ; i < obstacleGrid.length; i++){
            for(int j = 0; j < obstacleGrid[0].length; j++){
                obstacleGrid[i][j] ^= 1; // xor
                if(obstacleGrid[i][j] == 1){
                    if(i == 0 && j != 0) //check the position of the obstacle
                        obstacleGrid[i][j] = obstacleGrid[i][j-1];
                    if(i != 0 && j == 0)
                        obstacleGrid[i][j] = obstacleGrid[i-1][j];
                    if(i != 0 && j != 0)
                        obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1];
                }   
            }
        } 
        return obstacleGrid[obstacleGrid.length - 1][obstacleGrid[0].length - 1]; 
    }
}
