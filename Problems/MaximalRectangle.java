class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0) return 0;
        int result = 0;
        int len = matrix.length, wid = matrix[0].length;
        int[] width = new int[wid + 1];
        int[] hight = new int[wid + 1];
        
        for (int i = 0; i < len; i++) {
            Arrays.fill(width, 0);
            for (int j = 0; j < wid; j++) {
                width[j + 1] = matrix[i][j] == '0' ? 0 : width[j] + 1;
                hight[j + 1] = matrix[i][j] == '0' ? 0 : hight[j + 1] + 1;
                
                int k = 1, k2 = j + 1, h = hight[j + 1];
                while (k <= width[j + 1]) {
                    h = Math.min(h, hight[k2]);
                    result = Math.max(result, h * k);
                    k++;
                    k2--;
                }
            }
        }
        return result;        
    }
}
