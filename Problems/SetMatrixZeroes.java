class Solution {
    public void setZeroes(int[][] matrix) {
        int auxRow[]=new int[matrix.length];
        int auxColumn[]=new int[matrix[0].length];
        for(int i=0;i<matrix.length;i++){
             for(int j=0;j<matrix[0].length;j++){
                 if(matrix[i][j]==0){
                     auxRow[i]=99;
                     auxColumn[j]=99;
                 }
            }
        }
        for(int i=0;i<matrix.length;i++){
             for(int j=0;j<matrix[0].length;j++){
                 if(auxRow[i]==99 || auxColumn[j]==99 )
                     matrix[i][j]=0;
             }
        }
    }
}
