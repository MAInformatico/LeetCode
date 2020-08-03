class Solution {
    public int uniquePaths(int m, int n) {
        int[] table = new int[n];
        Arrays.fill(table, 1);
        for (int i = 1; i < m; ++i)
            for (int j = 1; j < n; ++j)
                table[j] += table[j - 1];
        return table[n - 1];
    }
}
